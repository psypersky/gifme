from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World2!"

@app.route("/ping", methods=["POST"])
def ping():
    return jsonify(
        response_type='in_channel',
        text='pong'
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)