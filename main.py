from flask import Flask, Response, render_template, send_from_directory
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your blueprints
from app.routes.wish import wish_bp
from app.routes.metadata import metadata_bp

# Set up Flask app
app = Flask(__name__, template_folder="templates")

# ✅ Homepage route (your full website)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Serve xrp-ledger.toml from the .well-known directory with correct MIME type
@app.route("/.well-known/xrp-ledger.toml")
def serve_toml():
    try:
        with open(".well-known/xrp-ledger.toml", "r") as f:
            toml_content = f.read()
        return Response(toml_content, mimetype="text/plain")
    except FileNotFoundError:
        return "xrp-ledger.toml not found", 404

# ✅ Register route blueprints (these don't interfere with your site)
app.register_blueprint(wish_bp)
app.register_blueprint(metadata_bp)

# ✅ Start the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
