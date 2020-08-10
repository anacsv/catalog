from app.model.base_model import BaseModel

class ShippingCountry(BaseModel):

    def __init__(self, name: str = '', imported: bool = 0, id: int = 0):
        self.__name = str(name)
        self.__imported = bool(imported)
        super().__init__(id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name:str):
        self.__name = name

    @property
    def imported(self) -> bool:
        return self.__imported

    @imported.setter
    def imported(self, imported:bool):
        self.__imported = imported

    def __str__(self):
        return f'{self.id};{self.name};{self.imported}'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'imported': self.imported
        }