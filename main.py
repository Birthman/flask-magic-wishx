from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from app.routes.wish import wish_bp

app = Flask(__name__, template_folder="templates")

app.register_blueprint(wish_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

