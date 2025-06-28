from flask import Flask, send_from_directory
from dotenv import load_dotenv

load_dotenv()

from app.routes.wish import wish_bp
from app.routes.metadata import metadata_bp

app = Flask(__name__, template_folder="templates")

# ✅ Serve the xrp-ledger.toml file at the root URL
@app.route('/xrp-ledger.toml')
def serve_toml():
    return send_from_directory('.', 'xrp-ledger.toml')

# ✅ Register route blueprints
app.register_blueprint(wish_bp)
app.register_blueprint(metadata_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
