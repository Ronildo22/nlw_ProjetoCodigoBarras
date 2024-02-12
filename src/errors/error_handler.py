from src.views.http_types.http_response import HttpResponse


class ErrorHandler:

    """
        Class with responsibility to exception errors handlers 
    """

    def handler_errors(self, error: Exception) -> HttpResponse:

        return HttpResponse(
            status_code=500,
            body={
                    'errors': [{
                        'title': 'Server Error',
                        'detail': str(error)
                    }]

            }
        )
