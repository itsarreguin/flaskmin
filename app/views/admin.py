"""All views for administrate users"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user

from app.models import Employee
from app.forms import EmployeeForm


mod = Blueprint('admin', __name__)


@mod.route('/dashboard/')
def dashboard():
    return render_template('admin/dashboard.html')


@mod.route('/employee/add/')
def new_employee():
    form = EmployeeForm()
    employees = Employee()
    
    if request.method == 'POST':
        employee = Employee.query.filter_by(username=form.username.data)
        
        if not employee:
            pass

    return render_template(
        'admin/add_employee.html', form=form, employees=employees
        )


@mod.route('/logout/')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))
