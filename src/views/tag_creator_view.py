from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:

    """
        Class with responsibility for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body
        print(body)

        # regra de negocio

        product_code = body['product_code']

        print(product_code)

        status_code = 200

        resp = {
            'Response': 'OK'

        }

        return HttpResponse(body=resp, status_code=status_code)
