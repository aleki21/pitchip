from flask import render_template
from . import auth
from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import SignUpForm,LoginForm
from .. import db
from ..email import mail_message

@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        print(user)
        if user is not None:
            user.verify_password(login_form.password.data)
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next')or url_for('main.index'))
        flash('Invalid username or password')

    return render_template('login.html',login_form = login_form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        #password = User.password(form.password.data)
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcome to Pitch perfect","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))


    return render_template('register.html',sign_up_form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))