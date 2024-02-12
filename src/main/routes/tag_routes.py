from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import ErrorHandler


tags_route_bp = Blueprint('tags_route', __name__)


@tags_route_bp.route('/create_tag', methods=['POST'])
def create_tags():

    try:

        body = request.json

        http_request = HttpRequest(body=body)

        tag_creator_view = TagCreatorView()
        http_response = tag_creator_view.validate_and_create(http_request)

    except Exception as e:
        error_handler = ErrorHandler()
        http_response = error_handler.handler_errors(e)

    return jsonify(http_response.product_code), http_response.status_code
