import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker

class BaseDao:

    def __init__(self, model_class):
        self.__connector = 'mysql+mysqlconnector'
        self.__hostname = 'mysql.padawans.dev'
        self.__username = 'padawans'
        self.__password = 'OTE2020'
        self.__database = 'padawans'
        self.__get_connection()
        self.__model_class = model_class

    def __get_connection(self):
        engine = db.create_engine(
            f'{self.__connector}://{self.__username}:{self.__password}@{self.__hostname}/{self.__database}')
        Session = db.orm.sessionmaker()
        Session.configure(bind=engine)
        self.__session = Session()

    # --- CRUD ----------------------

    # read
    def read(self, id: int = None):
        if id:
            return self.__session.query(self.__model_class).get(id)
        return self.__session.query(self.__model_class).all()

    #create
    def insert(self, sql_insert) -> int:
        self.__cursor.execute(sql_insert)
        self.__connection.commit()
        id = self.__cursor.lastrowid
        return id

    #update
    def update(self, sql_update):
        self.__cursor.execute(sql_update)
        self.__connection.commit()
        rows = self.__cursor.rowcount
        return rows

    #delete
    def delete(self, sql_delete) -> int:
        self.__cursor.execute(sql_delete)
        self.__connection.commit()
        rows = self.__cursor.rowcount
        return rows
