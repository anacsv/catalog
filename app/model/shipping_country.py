#id, name, imported
from app.model.base_model import BaseModel

class ShippingCountry(BaseModel):

    def __init__(self, name: str, imported: str, id: int = 0):
        self.__name = name
        self.__imported = imported
        super().__init__(id = id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def imported(self) -> str:
        return self.__imported

    @imported.setter
    def imported(self, imported:str):
        self.__imported = imported