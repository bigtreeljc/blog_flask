from flask import render_template, Flask, url_for
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

@app.route("/register")
def register():
  form = RegistrationForm()
  return render_template('register.html', title="Register",
            form=form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title="Login",
            form=form)




if __name__ == "__main__":
  app.run(debug=True)

