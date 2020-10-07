from flask import Blueprint, jsonify

blueprint = Blueprint('public', __name__)


@blueprint.route('/healthcheck')
def healthcheck():
    return 'healthy'


@blueprint.route("/ping", methods=["POST"])
def ping():
    return jsonify(
        response_type='in_channel',
        text='pong'
    )
