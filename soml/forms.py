from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired

class ImageForm(FlaskForm):
    image = FileField(validators=[FileRequired()])
    name = StringField()
    creator = StringField()
