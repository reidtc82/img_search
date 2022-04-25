from fileinput import filename
from app import app, forms

# from app.forms import UploadForm
import os
from flask import url_for, redirect, render_template, flash, request
from werkzeug.utils import secure_filename


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
