import logging

from flask import Flask, send_from_directory

from main.show import show_blueprint

from loader.download import download_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(show_blueprint)
app.register_blueprint(download_blueprint)

logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
