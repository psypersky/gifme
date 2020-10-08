from flask import Blueprint, jsonify

blueprint = Blueprint('public', __name__, url_prefix='/health')


@blueprint.route('/check', methods=['GET'])
def healthcheck():
    return 'healthy'


@blueprint.route("/ping", methods=['POST'])
def ping():
    return jsonify(
        response_type='in_channel',
        text='pong'
    )
