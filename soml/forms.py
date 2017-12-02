from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(message = 'Username missing!')])
	password = PasswordField('password', validators=[InputRequired(message = 'Password missing!')])
	new_user = BooleanField('new_user')


class ProfileForm(FlaskForm):
	delete = BooleanField('delete_image')










class ImageForm(FlaskForm):

    image_url = StringField('image_url')
    image_upload = FileField('image_upload')
    image_name = StringField('image_name', validators=[InputRequired(message = 'Image name missing!')])

    def validate(self):
        if not FlaskForm.validate(self):
        	return False
        if bool(self.image_url.data) ^ bool(self.image_upload.data):
        	return True
        elif bool(self.image_url.data) and bool(self.image_upload.data):
        	self.image_url.errors.append('Local image upload field is also populated!')
        	self.image_upload.errors.append('URL image download field is also populated!')
        	return False
        elif not bool(self.image_url.data) and not bool(self.image_upload.data):
         	self.image_url.errors.append('Please populate an upload method!')
        	self.image_upload.errors.append('Please populate an upload method!')
