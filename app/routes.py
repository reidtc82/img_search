from app import app, forms

# from app.forms import UploadForm
from flask import url_for, redirect, render_template
from werkzeug.utils import secure_filename


@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/upload", methods=["GET", "POST"])
def upload():
    form = forms.UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save("uploads/" + filename)
        return redirect(url_for("upload"))

    return render_template("image_submission.html", form=form)
