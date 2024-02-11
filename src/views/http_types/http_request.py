from typing import Dict


class HttpRequest:

    """
        Class with responsibility to store components HTTP(header, body, query_params)
    """

    def __init__(self, header: Dict = None, body: Dict = None, query_params: Dict = None) -> None:


        self.header = header
        self.body = body
        self.query_params = query_params
