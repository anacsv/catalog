#orm - Object-Relational-Mapping
# SQLAlchemy
# pip3 install sqlalchemy - pre-requisito connector (mysql-connector-python)
# pip freeze > requirements.txt

import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.model.base_model import BaseModel

Base = declarative_base()


class ProductCategory(Base, BaseModel):

    __tablename__ = 'product_category'
    __name = db.Column('name', db.String(length=64))
    __description = db.Column('description', db.String())

    def __init__(self, name: str = "", description: str = "", id: int = 0):
        self.__name = name
        self.__description = description
        # super().__init__(id=id)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = str(name)

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = str(description)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


# ==== Usando o orm
# ------ Dados de acesso a base de dados
connector = 'mysql+mysqlconnector'
hostname = 'mysql.padawans.dev'
username = 'padawans'
password = 'OTE2020'
database = 'padawans'

# ------ Criação da engine de conexão passando as informações de conetor e os acessos a base
engine = db.create_engine(f'{connector}://{username}:{password}@{hostname}/{database}')
# ------ Criando um tipo de dado que criará uma sessão de banco de dados
Session = db.orm.sessionmaker()
# ------ Configurando a sessão de banco para usar a engine de conexão
Session.configure(bind=engine)
# ------ Criando uma sessão com o banco de dados
session = Session()

# ----- acessando a tabela e listando seus dados em formato de objeto Python
# crud
# -- lista all

def list(id=None):
    if id:
        return session.query(ProductCategory).get(id)
    return session.query(ProductCategory).all()

def create(model:ProductCategory):
    session.add(model)
    session.commit()
    print('id:', model.id)

def update(model:ProductCategory):
    session.merge(model)
    session.commit()

def delete(id:int):
    model = list(id)
    session.delete(model)
    session.commit()

pc = ProductCategory('transformers Xaomi/Apple', 'roteadores')
create(pc)
