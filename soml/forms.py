from flask_wtf import FlaskForm
from wtforms import Field, BooleanField, HiddenField, StringField, PasswordField, SelectField, SelectMultipleField, SubmitField, widgets
from wtforms.compat import text_type
from wtforms.validators import InputRequired, StopValidation, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import IMAGES
from flask_login import current_user
from soml.utils import validate_image_url

class VoteForm(FlaskForm):
    shitpic = HiddenField('shitpic_uuid')
    upvote = SubmitField('vote up')
    downvote = SubmitField('vote down')

# handles login
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(message = 'Username missing!')])
    password = PasswordField('password', validators=[InputRequired(message = 'Password missing!')])
    new_user = BooleanField('new_user')

# generates multiple-select table of images with preview
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
                #forms img tag for preview
                image_html = '<img src="shitpic/get/' + str(subfield.data) + '">' + '' + '</img>'
                #adds img tag to generation
                html.append('<tr><th>%s%s</th><td>%s%s</td></tr>' % (text_type(subfield.label) + ':', text_type(image_html), hidden, text_type(subfield)))
                hidden = ''
        if self.with_table_tag:
            html.append('</table>')
        if hidden:
            html.append(hidden)
        return widgets.HTMLString(''.join(html))

# multiple selection field(s) with checkboxes for choices
class MultiCheckboxField(SelectMultipleField):
    widget = ImageTableWidget()
    option_widget = widgets.CheckboxInput()

# form for user's profile with multiple selectino of images
class ProfileForm(FlaskForm):
    delete = MultiCheckboxField('delete_image')
    def __init__(self, choices, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.delete.choices = choices

# ensures upload or url download fields are exclusively populated
def validate_upload_fields(self, form):
    if form.image_url.data and form.image_upload.data:
        raise StopValidation('Both URL and upload populated!')
    elif not form.image_url.data and not form.image_upload.data:
        raise StopValidation('Populate either URL or file upload!')

# field for url to download
# checks upload field not also populated
# checks url syntax is valid
# checks actual url is valid
class ImageUrlField(StringField):
    def pre_validate(self, form,):
        validate_upload_fields(self, form)
        if self.data:
            url_validator = URL(require_tld=True, message = 'That URL doesn\'t look right!')
            url_validator(form, self)
            validate_image_url(form.image_url.data)

# field for image upload
# checks url download not also populated
# checks file is present
# checks file extension is valid
class ImageFileField(FileField):
    def pre_validate(self, form,):
        validate_upload_fields(self, form)
        if self.data:
            file_validator = FileRequired(message = 'File is missing!')
            file_validator(form, self)
            file_ext_validator = FileAllowed(upload_set = IMAGES, message = 'File extension is incorrect!')
            file_ext_validator(form, self)

# form for image upload
class ImageUploadForm(FlaskForm):
    image_url = ImageUrlField('image_url', validators = [])
    image_upload = ImageFileField('image_upload', validators = [])
    image_name = StringField('image_name', validators=[InputRequired(message = 'Shitpic needs a name!')])
