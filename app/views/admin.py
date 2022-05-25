"""All views for administrate users"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user

from app.models import Admin, Employee
from app.forms import EmployeeForm
from db.settings import db_session
from app import login_manager


mod = Blueprint('admin', __name__)


@login_manager.user_loader
def loader_user():
    return db_session.query(Admin).filter(Admin.id).first()


@mod.route('/dashboard/')
@login_required
def dashboard():
    employees = db_session.query(Employee).order_by(Employee.created_at)

    return render_template('admin/dashboard.html', employees=employees)


@mod.route('/dashboard')
def dashboard_redirect():
    return redirect(url_for('admin.dashboard'))


@mod.route('/employee/add/', methods=['GET', 'POST'])
@login_required
def new_employee():
    form = EmployeeForm(request.form)
    
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        
        employee = db_session.query(Employee).filter(Employee.username == username).first()
        
        if not employee:
            new_employee = Employee(
                firstname = first_name,
                lastname = last_name,
                username = username,
                email = email
            )

            db_session.add(new_employee)
            db_session.commit()

            flash(f'{first_name} added successfully')

            return redirect(url_for('admin.dashboard'))

        else:
            flash('Employee username already exist')

    return render_template('admin/add_employee.html', form=form)


@mod.route('/employee/<username>/edit/', methods=['GET', 'POST'])
@login_required
def edit_employee(username: str):
    form = EmployeeForm(request.form)
    employee = db_session.query(Employee).filter(Employee.username == username).one()
    
    if request.method == 'POST':
        employee.first_name = request.form['first_name']
        employee.last_name = request.form['last_name']
        employee.username = request.form['username']
        employee.email = request.form['email']
        
        try:
            db_session.add(employee)
            db_session.commit()
            
            flash(f'{employee.username} updated succesfully')
            
            return redirect(url_for('admin.dashboard'))

        except:
           flash('Update error. Try again')
        
        finally:
            db_session.close()
    
    return render_template('admin/edit_employee.html', form=form, employee=employee)


@mod.route('/employee/<username>/delete/')
@login_required
def delete_employee(username: str):
    db_session.query(Employee).filter(Employee.username == username).delete()
    db_session.commit()

    flash(f'{username.capitalize()} was deleted correctly')

    return redirect(url_for('admin.dashboard'))


@mod.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))