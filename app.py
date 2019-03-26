from flask import render_template, Flask, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fba677308863bd0e0466508e56bc2fd7'

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
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f"Account created for {form.username.data}!", 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title="Register",
            form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
  else:
    flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title="Login",
            form=form)




if __name__ == "__main__":
  app.run(debug=True)

