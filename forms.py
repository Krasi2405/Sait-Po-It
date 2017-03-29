from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Regexp, Length


class AdminLoginForm(Form):
	username = StringField("Username", validators = [
		Regexp(r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only."))])
	
	password = PasswordField("Password", validators = [
		DataRequired(), 
		Length(min = 8)])


