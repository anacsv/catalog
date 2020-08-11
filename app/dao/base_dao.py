import mysql.connector as connector

class BaseDao:

    def __init__(self):
        self.__hostname = 'mysql.padawans.dev' 
        self.__username = 'padawans' 
        self.__password = 'OTE2020' 
        self.__database = 'padawans' 
        self.__get_connection()

    def __get_connection(self):
        self.__connection = connector.connect(
                        host = self.__hostname
                        ,user = self.__username
                        ,passwd = self.__password
                        ,db = self.__database
                    )   
        self.__cursor = self.__connection.cursor()    

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
    def read(self, sql_select:str):
        if 'where id'.lower() in sql_select.lower():
            return self.__read_by_id(sql_select)
        return self.__read_all(sql_select)

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
        return self.__create_message('Alterado com sucesso!', 'success')

    #delete
    def delete(self, sql_delete) -> int:
        self.__cursor.execute(sql_delete)
        self.__connection.commit()
        rows = self.__cursor.rowcount
        return rows
