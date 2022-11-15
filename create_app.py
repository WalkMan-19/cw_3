from flask import Flask
from posts.views import posts_blueprint
from api.api_blueprint import api_blueprint


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    app.register_blueprint(posts_blueprint)
    app.register_blueprint(api_blueprint)
    return app
