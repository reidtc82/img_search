from fileinput import filename
from app import app, forms, db
from app.models import Image

# from app.forms import UploadForm
import os
from flask import url_for, redirect, render_template, flash, request
from werkzeug.utils import secure_filename


@app.before_first_request
def before_first_request():
    app.logger.info("Here I am!")
    # Check that database is empty and if so download image dataset and fill it in


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = forms.UploadForm()

    if form.validate_on_submit():
        f = form.img_file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], "uploaded_images", filename))
        return redirect(url_for("index"))

    return render_template("image_submission.html", form=form)
