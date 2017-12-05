from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, StopValidation, URL
from flask_wtf.file import FileField, FileRequired

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(message = 'Username missing!')])
	password = PasswordField('password', validators=[InputRequired(message = 'Password missing!')])
	new_user = BooleanField('new_user')


class ProfileForm(FlaskForm):
	delete = BooleanField('delete_image')


class ImageUrlField(StringField):
    def pre_validate(self, form):
    	print 'prevalidating', self

    	valid = True

        if bool(form.image_url.data) ^ bool(form.image_upload.data):
        	valid = True
        elif bool(form.image_url.data) and bool(form.image_upload.data):
        	message = 'Both URL and upload populated!'
        	valid = False
        elif not bool(form.image_url.data) and not bool(form.image_upload.data):
        	message = 'Populate either URL or file upload!'
        	valid = False

    	if not valid:
    		raise StopValidation(message)	

class ImageForm(FlaskForm):
	image_url = ImageUrlField('image_url', validators=[URL()])
	image_upload = FileField('image_upload')
	image_name = StringField('image_name', validators=[InputRequired(message = 'Image name missing!')])
