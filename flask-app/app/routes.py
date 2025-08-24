from flask import Blueprint, request, jsonify, send_file
from .s3_utils import upload_file_to_s3, list_files_in_s3, download_file_from_s3
from .rekognise_utils import analyze_image
import io

routes = Blueprint("routes", __name__)

@routes.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    url = upload_file_to_s3(file, file.filename)
    return jsonify({"message": "Upload successful", "url": url}), 201

@routes.route("/files", methods=["GET"])
def list_files():
    files = list_files_in_s3()
    return jsonify({"files": files})

@routes.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    file_content = download_file_from_s3(filename)
    if file_content is None:
        return jsonify({"error": "File not found"}), 404

    return send_file(
        io.BytesIO(file_content),
        download_name=filename,
        as_attachment=True
    )

@routes.route("/analyse", methods=["POST"])
def analyse_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    upload_file_to_s3(file, file.filename)
    return analyze_image(file.filename)