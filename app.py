from flask import Flask, render_template, url_for, redirect, g, flash
from flask_bcrypt import check_password_hash
from flask_login import LoginManager, login_user, logout_user, current_user, login_required


import forms
import models


DEBUG = True
app = Flask(__name__)

app.secret_key = 'qwduhequfh9832h8fjoinad988913@10k2def4t3'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.Admin.get(models.Admin.id == userid)
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
	form = forms.AdminLoginForm()
	if form.validate_on_submit():
		try:
			admin = models.Admin.get(form.username.data == models.Admin.username)
			if(check_password_hash(admin.password, form.password.data)):
				login_user(admin)
				flash("Welcome back {}!".format(admin.username), "success")
				return redirect(url_for("admin_panel"))
			else:
				flash("Wrong username or password. Please try again.", "danger")	
		except models.DoesNotExist:
			flash("Wrong username or password. Please try again.", "danger")

	return render_template("login.html", form = form)

@app.route("/logout")
@login_required
def logout():
	logout_user()
	flash("You've been successfully logged out!", "success")
	return redirect(url_for("index"))

@app.route("/admin")
@login_required
def admin_panel():
	return render_template("admin_panel.html")

if __name__ == "__main__":
    models.initialize()
    try:
        models.Admin.create_admin(
            username = "KeePo",
            password = "password")

        models.Admin.create_admin(
        	username = "admin",
        	password = "admin123")
    except:
    	pass


    app.run(debug = DEBUG)