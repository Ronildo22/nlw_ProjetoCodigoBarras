
from unittest.mock import patch
from src.facade.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

@patch.object(BarcodeHandler, 'create_barcode')
def test_create(mock_create_barcode):
    mock_value = 'image_path'

    mock_create_barcode.return_value = mock_value

    tag_creator_controler = TagCreatorController()
    result = tag_creator_controler.create(mock_value)

    assert isinstance(result, dict)
    assert 'data' in result
    assert 'count' in result
    assert 'path' in result

    assert result['data'] == 'Tag Image'
    assert result['count'] == 1
    assert result['path'] == f'{mock_value}.png'
