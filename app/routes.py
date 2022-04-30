from fileinput import filename
from app import app, forms, db
from app.models import Image

# from app.forms import UploadForm
import os
from flask import url_for, redirect, render_template, flash, request
from werkzeug.utils import secure_filename

from app.image_loader import ImageLoader


@app.before_first_request
def before_first_request():
    app.logger.info("Initializing")
    # Check that database is empty and if so download image dataset and fill it in
    images = Image.query.all()
    if not images:
        app.logger.info("Images database is empty")
        img_gen = ImageLoader(debug=True)
        app.logger.info("Filling database")
        for img_loc in img_gen:
            db.session.add(Image(image_location=img_loc))
            db.session.commit()


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
        f.save(os.path.join(app.config["ROOT_FOLDER"], "uploaded_images", filename))
        return redirect(url_for("index"))

    return render_template("image_submission.html", form=form)
