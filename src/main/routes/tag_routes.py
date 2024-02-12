from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import ErrorHandler
from src.validators.tag_creator_validator import TagCreatorValidator


tags_route_bp = Blueprint('tags_route', __name__)


@tags_route_bp.route('/create_tag', methods=['POST'])
def create_tags():

    try:

        TagCreatorValidator.tag_creator_validator(request)

        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        http_response = tag_creator_view.validate_and_create(http_request)

    except Exception as e:
        http_response = ErrorHandler.handler_errors(e)

    return jsonify(http_response.product_code), http_response.status_code
