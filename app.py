from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Supported file extensions
ALLOWED_EXTENSIONS = {
    "pdf",
    "docx",
    "jpg",
    "jpeg",
    "png",
    "bmp",
    "tiff",
    "tif"
}


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return jsonify({
        "status": "Running",
        "message": "Document Uploader API"
    })
