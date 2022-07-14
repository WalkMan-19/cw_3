from flask import Flask
from posts.views import posts_blueprint
from api.api import api_blueprint


app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run()
