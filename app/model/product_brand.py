from base_model import BaseModel

class ProductBrand(BaseModel):

    def __init__(self, name: str = '',
                fullname: str = '', id:int = 0):
        self.__name = name
        self.__fullname = fullname
        super().__init__(id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def fullname(self) -> str:
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname: str) -> None:
        self.__fullname = fullname

    def __str__(self):
        return f'{self.id};{self.name};{self.fullname}'