from flask import Blueprint, request, jsonify

blueprint = Blueprint('image', __name__, url_prefix='/image')
"""
Slack sends a POST message with Content-type: application/x-www-form-urlencoded

curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
"""


@blueprint.route("/gifme", methods=["POST"])
def gifme():
    cmd_text = request.form.get('text')

    # return str(request.args)
    return jsonify(
        response_type='in_channel',
        text=str(request.form)
    )
    # return jsonify(
    #     response_type='in_channel',
    #     attachments=[
    #         {
    #             "fallback": "sad but true gif image",
    #             "image_url": "https://gifme-public.s3.us-east-2.amazonaws.com/ezgif.com-gif-maker.gif"
    #         }
    #     ]
    # )

