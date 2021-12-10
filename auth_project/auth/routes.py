import re
from flask import render_template,flash,redirect,url_for,request
from . import auth
from flask_login import login_user,logout_user,current_user
from auth_project import db,bcrypt
from auth_project.models import User
from .forms import RegistrationForm,LoginForm

@auth.route('/register',methods = ['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('pages.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user_email = User.query.filter_by(email=form.email.data).first()
        if user_email:
            flash('Email Already Exists','success')
            return redirect(url_for('auth.register'))
        hashedpassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data,username=form.username.data,password=hashedpassword)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created for {form.username.data}','success')
        return redirect(url_for('pages.home'))
    return render_template('auth/register.html',title='Sign Up',form=form)

@auth.route("/login",methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        flash('Your Logged in already.','success')
        return redirect(url_for('pages.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash(f'Login success for {form.email.data}','success')
            return redirect(next_page) if next_page else redirect(url_for('pages.home'))
        flash('Login Unsuccessful Check email and password','danger')
    return render_template('auth/login.html',form=form,title='Login')

@auth.route('/logout',methods = ['POST','GET'])
def logout():
    if request.method == 'POST':
        logout_user()
        flash('SuccessFully Logged Out','success')
        return redirect(url_for('pages.home'))
    else:
        return render_template('auth/logout.html')