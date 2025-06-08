from flask import Blueprint, send_from_directory

metadata_bp = Blueprint("metadata", __name__)

@metadata_bp.route("/xmc.json")
def serve_xmc_metadata():
    return send_from_directory("static/metadata", "xmc.json")
