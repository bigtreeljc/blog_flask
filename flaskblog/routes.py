from flask import render_template, Flask, url_for, flash, redirect, request

from .models import User, Post
from .forms import RegistrationForm, LoginForm
from . import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required

posts = [
  {
    "author": "Lu Junchen",
    "title": "title 1",
    "content": "blog post content",
    "date_posted": "2018-04-21"
  },
  {
    "author": "li Pan",
    "title": "title 2",
    "content": "blog post content",
    "date_posted": "2018-04-23"
  }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html", posts=posts, title="jlu56")

@app.route("/about")
def about():
  return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
        return redirect(url_for('home'))

  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f"Account created for {form.username.data}!", 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title="Register",
            form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
        return redirect(url_for('home'))

  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title="Login",
            form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
