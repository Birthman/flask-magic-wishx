import os
from flask import Blueprint, send_from_directory

metadata_bp = Blueprint("metadata", __name__)

@metadata_bp.route("/.well-known/xrp-ledger.toml")
def serve_toml():
    toml_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".well-known")
    return send_from_directory(toml_path, "xrp-ledger.toml", mimetype='text/plain')
)
