from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired

class RegisterForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()])
	password = PasswordField('password', validators=[InputRequired()])

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired()])
	password = PasswordField('password', validators=[InputRequired()])
	remember = BooleanField('remember me')

class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired()])
    name = StringField()
    creator = StringField()