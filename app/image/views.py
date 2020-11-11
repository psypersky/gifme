from flask import Blueprint, request, jsonify

from app.lib.s3 import list_bucket_object_keys

blueprint = Blueprint('image', __name__, url_prefix='/image')
"""
Slack sends a POST message with Content-type: application/x-www-form-urlencoded

curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
"""


@blueprint.route("/gifme", methods=["POST"])
def gifme():
    cmd_text = request.form.get('text')
    cmd_arr = cmd_text.split()

    if (len(cmd_arr) == 1):
        cmd = cmd_arr[0]

        if (cmd == 'ls'):
            # TODO: aws list

            keys_list = list_bucket_object_keys()

            keys_txt = '\n'.join(keys_list)

            return jsonify(
                response_type='in_channel',
                text=keys_txt
            )
        
        return jsonify(
            response_type='in_channel',
            text='Command not found or incorrect, please RTFD :)'
        )


    # bucket = cmd_arr[0]
    # image = cmd_arr[1]
    # TODO: get image from s3
    # return str(request.args)

    print(str(request.form))
    return jsonify(
        response_type='in_channel',
        text='We are looking for help in Upty, if you want to learn some python in your free time, please contact @ruben'
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
