"""All views for administrate users"""

from hashlib import new
from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user

from app.models import Employee
from app.forms import EmployeeForm
from db.settings import db_session


mod = Blueprint('admin', __name__)


@mod.route('/dashboard/')
def dashboard():
    employees = db_session.query(Employee).order_by(Employee.created_at)

    return render_template('admin/dashboard.html', employees=employees)


@mod.route('/dashboard')
def dashboard_redirect():
    return redirect(url_for('admin.dashboard'))


@mod.route('/employee/add/', methods=['GET', 'POST'])
def new_employee():
    form = EmployeeForm(request.form)
    
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        
        employee = db_session.query(Employee).filter(Employee.username == username)
        
        if not employee:
            new_employee = Employee(
                firstname = first_name,
                lastname = last_name,
                username = username,
                email = email
            )
            
            try:
                db_session.add(new_employee)
                db_session.commit()

                flash(f'{first_name} added successfully')
                
                return redirect(url_for('admin.dashboard'))
            
            except:
                flash('Creation error. Try again')
                return redirect(url_for('admin.dashboard'))

        else:
            flash('Employee already exist')

    return render_template('admin/add_employee.html', form=form)


@mod.route('/employee/<username>/edit/', methods=['GET', 'POST'])
def edit_employee(username: str):
    pass


@mod.route('/employee/<username>/delete/')
def delete_emplyee(username: str):
    pass


@mod.route('/logout/')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))