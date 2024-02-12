class HttpUnprocessableEntityError(Exception):

    """
        Class with responsibility for handler error HTTP 422 (Unprocessable Entity)
    """

    def __init__ (self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessbleEntity'
        self.status_code = 422
