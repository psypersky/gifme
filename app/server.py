from flask import Flask, jsonify, request

from app import public, image

app = Flask(__name__)

app.register_blueprint(public.views.blueprint)
app.register_blueprint(image.views.blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

