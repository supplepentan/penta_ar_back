import base64
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
from libs.ar.face_extruct import FaceExtruct
from libs.making_aping.app import Movie
from PIL import Image
from werkzeug.utils import secure_filename

ar = Blueprint(
    "ar",
    __name__,
    template_folder="templates",
    static_folder="templates/static",
)

ALLOWED_EXTENSIONS = {"avi", "mpg", "jpg"}
UPLOAD_FOLDER = "upload"


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@ar.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("ar/index.html")
    if request.method == "POST":
        contents = request.files["file"]
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
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
            subprocess.run(
                ["ffmpeg", "-i", path, os.path.join(UPLOAD_FOLDER, "out.apng")]
            )
            return {"return": "post"}
        return redirect(request.url)


@ar.route("/test", methods=["GET", "POST"])
def test():
    downloadFileName = "retrun.png"
    downloadFile = os.path.join("..", "upload", "return_image.png")
    if request.method == "GET":
        return send_file(
            downloadFile,
            as_attachment=True,
            attachment_filename=downloadFileName,
            mimetype="image/png",
        )
    if request.method == "POST":
        print(request.files["file"])
        return send_file(
            downloadFile,
            as_attachment=True,
            attachment_filename=downloadFileName,
            mimetype="image/png",
        )


@ar.route("/face_extruct", methods=["GET", "POST"])
def face_extruct():
    if request.method == "GET":
        return {"return": "GET"}
    if request.method == "POST":
        face_extruct_instance = FaceExtruct()
        contents = request.files["file"]
        input_path = os.path.join("upload", "input.jpg")
        output_path = os.path.join("upload", "output.jpg")
        # image = Image.open(BytesIO(contents)).convert("RGB")
        image = Image.open(contents).convert("RGB")
        image.save(input_path)
        output_image = face_extruct_instance.run_alignment(input_path)
        output_image.save(output_path)
        with open(output_path, "rb") as image_file:
            data = base64.b64encode(image_file.read()).decode("utf-8")
        return send_file(
            os.path.join("..", "upload", "output.jpg"),
            as_attachment=True,
            attachment_filename="face_extruct.jpg",
            mimetype="image/jpg",
        )


"""
        print(request.files["file"])
        return send_file(
            downloadFile,
            as_attachment=True,
            attachment_filename=downloadFileName,
            mimetype="image/png",
        )



    if request.method == "GET":
        return render_template("face_ext/index.html")
    if request.method == "POST":
        contents = request.files["file"]
        input_path = os.path.join("output", "face_ext", "input.jpg")
        output_path = os.path.join("output", "face_ext", "output.jpg")
        # image = Image.open(BytesIO(contents)).convert("RGB")
        image = Image.open(contents).convert("RGB")
        image.save(input_path)
        output_image = run_alignment(input_path)
        output_image.save(output_path)
        with open(output_path, "rb") as image_file:
            data = base64.b64encode(image_file.read()).decode("utf-8")
        return render_template("face_ext/index.html", data=data)
        
"""
