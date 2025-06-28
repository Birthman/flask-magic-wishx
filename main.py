from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os

load_dotenv()

from app.routes.wish import wish_bp
from app.routes.metadata import metadata_bp

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return "✅ MagicDev is live! Welcome to the JIN token site."

@app.route("/xrp-ledger.toml")
def serve_toml():
    return send_from_directory(".", "xrp-ledger.toml")

app.register_blueprint(wish_bp)
app.register_blueprint(metadata_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

