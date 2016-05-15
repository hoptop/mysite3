from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    name = StringField('who are you', validators=[DataRequired()])
    submit = SubmitField('Submit')