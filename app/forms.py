from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    img_file = FileField("Image File", validators=[DataRequired()])

    submit = SubmitField("Search")
