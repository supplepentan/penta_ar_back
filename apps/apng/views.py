import os
import subprocess

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    send_file,
    send_from_directory,
    url_for,
)
from werkzeug.utils import secure_filename

apng = Blueprint(
    "apng",
    __name__,
    template_folder="templates",
    static_folder="templates/static",
)

ALLOWED_EXTENSIONS = {"jpg", "jpge"}
UPLOAD_FOLDER = "upload"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@apng.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("apng/index.html")
    if request.method == "POST":
        contents = request.files["file"]
        # check if the post request has the file papngt
        if "file" not in request.files:
            flash("No file papngt")
            return redirect(request.url)
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path)
            subprocess.run([])
            return {"return": "post"}
        return redirect(request.url)


@apng.route("/apng_make", methods=["GET", "POST"])
def apng_make():
    if request.method == "GET":
        return {"return": "GET"}
    if request.method == "POST":
        from libs.making_aping.app import ApngMaker

        apngmaker = ApngMaker()
        return {"return": "POST"}
