from app.model.base_model import BaseModel


class ProductBrand(BaseModel):

    def __init__(self, name: str = '',
                 full_name: str = '', id:int = 0):
        self.__name = name
        self.__full_name = full_name
        super().__init__(id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = str(name)

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, fullname: str) -> None:
        self.__full_name = str(full_name)

    def __str__(self):
        return f'{self.id};{self.name};{self.full_name}'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.full_name
        }