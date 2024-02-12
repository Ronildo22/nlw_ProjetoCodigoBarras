from src.facade.barcode_handler import BarcodeHandler

class TagCreatorController:

    """
        Class with responsibility for implement business rules
    
    """

    def __create_tag(self, product_code: str) -> str:

        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

    def __format_response(self, path_from_tag: str) -> dict:

        resp = {
            'data': 'Tag Image',
            'count': 1,
            'path': f'{path_from_tag}.png'
        }

        return resp


    def create(self, producte_code: str) -> dict:

        path_from_tag =  self.__create_tag(producte_code)
        formated_response =  self.__format_response(path_from_tag)

        return formated_response
