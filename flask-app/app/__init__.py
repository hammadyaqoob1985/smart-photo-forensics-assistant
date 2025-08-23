from flask import Flask

def create_app():
    app = Flask(__name__)

    # Use relative import
    from .routes import routes
    app.register_blueprint(routes)

    return app
