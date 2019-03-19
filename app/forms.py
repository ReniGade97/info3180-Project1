from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class ProfileForm(FlaskForm):
    firstname   = StringField   ('First Name',  validators=[InputRequired()])
    lastname    = StringField   ('Last Name',   validators=[InputRequired()])
    email       = StringField   ('Email',       validators=[InputRequired()])
    location    = StringField   ('Location',    validators=[InputRequired()])
    gender      = SelectField    ('Gender',     choices= [('M', 'Male'), ('F', 'Female')])
    biography   = TextAreaField ('Biography',   validators=[InputRequired()])
    photo       = FileField     ('Photo',       validators=[FileRequired()])