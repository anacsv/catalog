from app.model.base_model import BaseModel
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductBrand(Base, BaseModel):

    __tablename__ = 'product_brand'
    __name = db.Column('name', db.String(length=64))
    __full_name = db.Column('full_name', db.String())

    def __init__(self, name: str = '',
                 full_name: str = ''):
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
    def full_name(self, full_name: str) -> None:
        self.__full_name = str(full_name)

    def __str__(self):
        return f'{self.id};{self.name};{self.full_name}'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'full_name': self.full_name
        }