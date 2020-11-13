from flask import Blueprint, request, jsonify

from app.lib.s3 import list_bucket_object_keys, check_if_image_exists

blueprint = Blueprint('image', __name__, url_prefix='/image')
"""
Slack sends a POST message with Content-type: application/x-www-form-urlencoded

curl -d "param1=value1&param2=value2" -X POST http://localhost:3000/data
"""


def command_not_found_res():
    return jsonify(
        response_type='in_channel',
        text='Command not found or incorrect, please RTFD :)'
    )


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

        return command_not_found_res()

    if (len(cmd_arr) == 2):
        ext = '.gif'
        folder = cmd_arr[0]
        image = cmd_arr[1]
        image_key = folder + '/' + image + ext
        img_exists = check_if_image_exists(image_key)

        if (img_exists):

            return jsonify(
                response_type='in_channel',
                attachments=[
                    {
                        "fallback": "a gif image",
                        "image_url": f'https://gifme-public.s3.us-east-2.amazonaws.com/{image_key}'
                    }
                ]
            )

        return jsonify(
            response_type='in_channel',
            text='Image not found :\'( try using "ls" command'
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
