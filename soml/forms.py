from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField
from wtforms.validators import InputRequired, StopValidation, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import IMAGES

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(message = 'Username missing!')])
	password = PasswordField('password', validators=[InputRequired(message = 'Password missing!')])
	new_user = BooleanField('new_user')

class ProfileForm(FlaskForm):
	delete = BooleanField('delete_image')


class ImageUrlField(StringField):
    def pre_validate(self, form):

        if form.image_url.data and not form.image_upload.data:
            url_validator = URL(message = 'BAD URL')
            url_validator(form, form.image_url)
        elif form.image_upload.data and not form.image_url.data:
            file_validator = FileRequired(message = 'NO FILE')
            file_validator(form, form.image_upload)
            file_ext_validator = FileAllowed(upload_set = IMAGES, message = 'BAD EXT')
            file_ext_validator(form, form.image_upload)
        elif bool(form.image_url.data) and bool(form.image_upload.data):
            raise StopValidation('Both URL and upload populated!')
        elif not bool(form.image_url.data) and not bool(form.image_upload.data):
        	raise StopValidation('Populate either URL or file upload!')
    			

class ImageForm(FlaskForm):
	image_url = ImageUrlField('image_url')
	image_upload = FileField('image_upload')
	image_name = StringField('image_name', validators=[InputRequired(message = 'Image name missing!')])
