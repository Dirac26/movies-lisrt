from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class MovieForm(FlaskForm):
    name =  StringField("Movie Name", validators=[DataRequired()])
    rating =  StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add Movie")