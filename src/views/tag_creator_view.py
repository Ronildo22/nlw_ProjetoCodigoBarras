from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:

    """
        Class with responsibility for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        product_code = body['product_code']

        tag_creator_controler = TagCreatorController()
        formatted_response = tag_creator_controler.create(product_code)

        status_code = 200

        return HttpResponse(body=formatted_response, status_code=status_code)
