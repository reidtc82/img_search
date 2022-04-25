from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from app import app

images = UploadSet("images", IMAGES, default_dest=lambda x: "images")
configure_uploads(app, images)


class UploadForm(FlaskForm):
    img_file = FileField(
        "Image File", validators=[FileRequired(), FileAllowed(images, "Images only!")]
    )
    submit = SubmitField("Search")
