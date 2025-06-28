from flask import Flask, Response, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import your blueprints
from app.routes.wish import wish_bp
from app.routes.metadata import metadata_bp

# Set up Flask app
app = Flask(__name__, template_folder="templates")

# ✅ Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Properly serve xrp-ledger.toml from `.well-known` folder with correct MIME type
@app.route("/xrp-ledger.toml")
def serve_toml():
    try:
        with open(".well-known/xrp-ledger.toml", "r") as f:  # <-- updated path here
            toml_content = f.read()
        return Response(toml_content, mimetype="text/plain")
    except FileNotFoundError:
        return "xrp-ledger.toml not found", 404

# ✅ Register blueprints
app.register_blueprint(wish_bp)
app.register_blueprint(metadata_bp)

# ✅ Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)





