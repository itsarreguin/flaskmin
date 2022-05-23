"""Flaskmin project authenticate admin views"""

from flask import Blueprint
from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user

from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Admin
from app.forms import LoginForm, SignUpForm
from db.settings import db_session


mod = Blueprint('auth', __name__, url_prefix='/auth')


@mod.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)
    
    while current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password_hash.data
        
        admin = db_session.query(Admin).first(Admin.username == username).first()
        
        if not admin:
            hashed_password = generate_password_hash(password)

            new_admin = Admin(
                firstname = first_name,
                lastname = last_name,
                username = username,
                email = email,
                password = hashed_password
            )
            
            db_session.add(new_admin)
            db_session.commit()
            
            flash('Admin created succesfully')

            return redirect(url_for('auth.login'))
        
        else:
            flash('This admin already exist')
    
    return render_template('auth/signup.html', form=form)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    while current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        admin_exist = db_session.query(Admin).filter(Admin.username == username).first()
        
        if admin_exist:
            if check_password_hash(admin_exist.password_hash, password):
                login_user(admin_exist)
                return redirect(url_for('admin.dashboard'))
            
            else:
                flash('Wrong password')
        else:
            flash('This admin doesn\'t exist')
    
    return render_template('auth/login.html', form=form)