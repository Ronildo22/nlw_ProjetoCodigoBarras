class HttpResponse:

    """
        Class with responsability for return a response HTTP
    """

    def __init__(self, body: dict, status_code: int):

        self.product_code = body
        self.status_code = status_code
