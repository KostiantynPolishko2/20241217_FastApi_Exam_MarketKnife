from fastapi import status

class KnifeException404(Exception):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND

    def __call__(self, name_obj: str, _property: str):
        self.detail = f'{name_obj.lower().capitalize()} \'{_property.upper()}\' is absent in db!'

weapons_exc404 = KnifeException404()