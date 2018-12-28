from flask import Flask
from flask_cors import CORS
from test import test_bp

__all__ = ["app"]


app = Flask("app")
app.register_blueprint(test_bp)


CORS(app, supports_credentials=True)
