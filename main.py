from flask import Flask, send_from_directory, render_template, Response
from dotenv import load_dotenv
import os

load_dotenv()

from app.routes.wish import wish_bp
from app.routes.metadata import metadata_bp

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/xrp-ledger.toml")
def serve_toml():
    try:
        return send_from_directory(".well-known", "xrp-ledger.toml", mimetype="text/plain")
    except FileNotFoundError:
        return "xrp-ledger.toml not found", 404

app.register_blueprint(wish_bp)
app.register_blueprint(metadata_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)




