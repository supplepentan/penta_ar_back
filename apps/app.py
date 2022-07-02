import subprocess

from flask import Flask, render_template, request
from flask_cors import CORS
from libs.ar.face_extruct import FaceExtruct

from apps.config import config


def create_app(config_key):
    app = Flask(__name__, static_folder="templates/static")
    app.config.from_object(config[config_key])
    CORS(app, origins=["http://localhost:3000"])

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            return render_template("index.html")
        else:
            return {"return": "post"}

    from apps.ar import views as ar_views

    app.register_blueprint(ar_views.ar, url_prefix="/ar")

    from apps.apng import views as apng_views

    app.register_blueprint(apng_views.apng, url_prefix="/apng")

    from apps.camera import views as camera_views

    app.register_blueprint(camera_views.camera, url_prefix="/camera")

    return app
