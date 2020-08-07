from app.model.base_model import BaseModel


class Product(BaseModel):

    def __init__(self, name: str = '', price: float = 0.0,
                 description: str = '', gtin='', product_condition_id=0,
                 brand_id=0, shipping_country_id=0, id: int = 0):
        self.__nome = name
        self.__preco = price
        self.__description = description
        self.__gtin = gtin
        self.__brand_id = brand_id
        self.__product_condition_id = product_condition_id
        self.__shipping_country_id = shipping_country_id
        super().__init__(id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = float(price)

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str) -> None:
        self.__description = str(description)

    @property
    def gtin(self) -> str:
        return self.__gtin

    @gtin.setter
    def gtin(self, gtin: str) -> None:
        self.__gtin = str(gtin)

    def __str__(self):
        return f'{self.id};{self.name};{self.price};{self.gtin};{self.__brand_id}; {self.__product_condition_id}; {self.__shipping_country_id}'

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'gtin': self.gtin,
            'brand_id': self.__brand_id,
            'product_condition_id': self.__product_condition_id,
            'shipping_country_id': self.__shipping_country_id
        }
