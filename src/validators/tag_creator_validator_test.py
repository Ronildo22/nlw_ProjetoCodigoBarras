from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import TagCreatorValidator



class MockRequest:

    """
        Class responsible for test of requests
    """

    def __init__(self, json):
        self.json = json


def test_tag_creator_validator():

    json = {
        'product_code': '1449'
    }

    req = MockRequest(json=json)
    TagCreatorValidator.tag_creator_validator(req)

def test_tag_creator_validator_with_error():

    json = {
            'product_code': 1449
        }

    req = MockRequest(json=json)

    try:
        TagCreatorValidator.tag_creator_validator(req)
        assert False
    except Exception as e:
        assert isinstance(e, HttpUnprocessableEntityError)
