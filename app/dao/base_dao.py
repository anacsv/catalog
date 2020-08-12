import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker
from app.model.product_category import ProductCategory

class BaseDao:

    def __init__(self):
        self.__connector = 'mysql+mysqlconnector'
        self.__hostname = 'mysql.padawans.dev'
        self.__username = 'padawans'
        self.__password = 'OTE2020'
        self.__database = 'padawans'
        self.__get_connection()

    def __get_connection(self):
        self.__engine = db.create_engine(
            f'{self.__connector}://{self.__username}:{self.__password}@{self.__hostname}/{self.__database}')
        Session = db.orm.sessionmaker()
        Session.configure(bind=self.__engine)
        self.__session = Session()

    # --- CRUD ----------------------
    #read_by_id
    def __read_by_id(self, sql_select):
        self.__cursor.execute(sql_select)
        result = self.__cursor.fetchone()
        return result

    #read_all
    def __read_all(self, sql_select) -> list:
        self.__cursor.execute(sql_select)
        result = self.__cursor.fetchall()
        return result

    #read
    def read(self, model_class, id: int = None):
        if id:
            return self.__session.query(model_class).get(id)
        breakpoint(self.__session)
        return self.__session.query(model_class).all()

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
