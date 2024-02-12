from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class TagCreatorValidator:

    """
        Class with responsibility for valide body request HTTP
    """

    @staticmethod
    def tag_creator_validator(request: any) -> None:

        body_validator = Validator({
            'product_code': {
                'type': 'string', 
                'required': True,
                'empty': False
            }
        })

        response = body_validator.validate(request.json)

        if response is False:
            raise HttpUnprocessableEntityError(body_validator.errors)
