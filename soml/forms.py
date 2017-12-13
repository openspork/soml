from flask_wtf import FlaskForm
from wtforms import Field, BooleanField, StringField, PasswordField, SelectFieldBase, SelectMultipleField, widgets
from wtforms.compat import text_type
from wtforms.validators import InputRequired, StopValidation, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import IMAGES
from flask_login import current_user
from soml.utils import validate_image_url

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message = 'Username missing!')])
    password = PasswordField('password', validators=[InputRequired(message = 'Password missing!')])
    new_user = BooleanField('new_user')

class ImageTableWidget(widgets.TableWidget):
    def __call__(self, field, **kwargs):
        html = []
        if self.with_table_tag:
            kwargs.setdefault('id', field.id)
            html.append('<table %s>' % widgets.html_params(**kwargs))
        hidden = ''
        for subfield in field:
            if subfield.type in ('HiddenField', 'CSRFTokenField'):
                hidden += text_type(subfield)
            else:
                image_html = '<img src="shitpic/get/' + str(subfield.data) + '">' + '' + '</img>'
                html.append('<tr><th>%s%s</th><td>%s%s</td></tr>' % (text_type(subfield.label) + ':', text_type(image_html), hidden, text_type(subfield)))
                hidden = ''
        if self.with_table_tag:
            html.append('</table>')
        if hidden:
            html.append(hidden)
        return widgets.HTMLString(''.join(html))

class MultiCheckboxField(SelectMultipleField):
    widget = ImageTableWidget()
    option_widget = widgets.CheckboxInput()

class ProfileForm(FlaskForm):
    delete = MultiCheckboxField('delete_image', description = 'url path')
    
    def __init__(self, choices, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.delete.choices = choices




        

def validate_upload_fields(self, form):
    if bool(form.image_url.data) and bool(form.image_upload.data):
        raise StopValidation('Both URL and upload populated!')
    elif not form.image_url.data and not form.image_upload.data:
        raise StopValidation('Populate either URL or file upload!')

class ImageUrlField(StringField):
    def pre_validate(self, form,):
        validate_upload_fields(self, form)
        if self.data:
            url_validator = URL(require_tld=True, message = 'That URL doesn\'t look right!')
            url_validator(form, self)
            validate_image_url(form.image_url.data)

class ImageFileField(FileField):
    def pre_validate(self, form,):
        validate_upload_fields(self, form)
        if self.data:
            file_validator = FileRequired(message = 'File is missing!')
            file_validator(form, self)
            file_ext_validator = FileAllowed(upload_set = IMAGES, message = 'File extension is incorrect!')
            file_ext_validator(form, self)

class ImageForm(FlaskForm):
    image_url = ImageUrlField('image_url', validators = [])
    image_upload = ImageFileField('image_upload', validators = [])
    image_name = StringField('image_name', validators=[InputRequired(message = 'Shitpic needs a name!')])
