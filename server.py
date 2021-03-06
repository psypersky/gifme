from flask import Flask, jsonify, request

from app import health, image

# from app.setting import *
# TODO: setup flask config using environ

app = Flask(__name__)

app.register_blueprint(health.views.blueprint)
app.register_blueprint(image.views.blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

