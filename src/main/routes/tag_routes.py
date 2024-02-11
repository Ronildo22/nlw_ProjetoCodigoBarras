from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView


tags_route_bp = Blueprint('tags_route', __name__)


@tags_route_bp.route('/create_tag', methods=['POST'])
def create_tags():

    body = request.json

    if isinstance(body, dict):

        http_request = HttpRequest(body=body)

        tag_creator_view = TagCreatorView()
        http_response = tag_creator_view.validate_and_create(http_request)

        return jsonify(http_response.product_code, http_response.status_code)

    else:

        resp_error = {
            'failed': 'Envie um componente json'
        }

        return jsonify(resp_error)
