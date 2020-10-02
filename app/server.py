from flask import Flask, jsonify, request

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


"""
Slack sends a POST message with Content-type: application/x-www-form-urlencoded

curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
"""


@app.route("/bale", methods=["POST"])
def bale():
    return jsonify(
        response_type='in_channel',
        attachments=[
            {
                "fallback": "sad but true gif image",
                "image_url": "https://gifme-public.s3.us-east-2.amazonaws.com/ezgif.com-gif-maker.gif"
            }
        ]
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
