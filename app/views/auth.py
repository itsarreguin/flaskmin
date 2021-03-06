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
    
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password_hash.data
        
        admin_exist = db_session.query(Admin).filter(Admin.username == username).first()
        
        if not admin_exist:
            hashed_password = generate_password_hash(password, method='sha256')

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
    
    while current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    return render_template('auth/signup.html', form=form)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    while form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = True if request.form.get('remember') else False

        admin = db_session.query(Admin).filter(Admin.username == username).first()

        while admin:
            if check_password_hash(admin.password_hash, password):
                login_user(admin, remember=remember)
                flash(f'Welcome back {admin.username}')

                return redirect(url_for('admin.dashboard'))
            
            else:
                flash('Wrong password')
                return redirect(url_for('auth.login'))

        if not admin:
            flash('This admin doesn\'t exist. Please sign up')
            return redirect(url_for('auth.signup'))

    while current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))

    return render_template('auth/login.html', form=form)