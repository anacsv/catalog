import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

from app.model.base_model import BaseModel

Base = declarative_base()

class ShippingCountry(Base, BaseModel):

    __tablename__ = 'shipping_country'
    __name = db.Column('name', db.String(length=64))
    __imported = db.Column('imported', db.Boolean())

    def __init__(self, name: str = '', imported: bool = 0):
        self.__name = str(name)
        self.__imported = bool(imported)

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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'imported': self.imported
        }

    # def __dict__(self):
    #     return {
    #         'id': self.id,
    #         'name': self.name,
    #         'imported': self.imported
    #     }