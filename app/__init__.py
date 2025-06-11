from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register wish routes
    from .routes.wish import wish_bp
    app.register_blueprint(wish_bp)

    # Register metadata routes
    from .metadata import metadata_bp
    app.register_blueprint(metadata_bp)

    return app
