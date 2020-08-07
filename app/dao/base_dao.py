import mysql.connector as connector

class BaseDao:

    def __init__(self):
        self.__hostname = 'mysql.padawans.dev' 
        self.__username = 'padawans' 
        self.__password = 'OTE2020' 
        self.__database = 'padawans' 
        self.__get_connection()
        
 
    def __get_connection(self):
        print('passando pelo get connect')
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
    def insert(self, sql_insert):
        self.__cursor.execute(sql_insert)
        self.__connection.commit()
        return self.__create_message('Salvo com sucesso!', 'success')

    #update
    def update(self, sql_update):
        self.__cursor.execute(sql_update)
        self.__connection.commit()
        return self.__create_message('Alterado com sucesso!', 'success')

    #delete
    def delete(self, sql_delete):
        self.__cursor.execute(sql_delete)
        self.__connection.commit()
        return self.__create_message('Deletado com sucesso!', 'success')





    def __create_message_text_from_list(self, fields):
        message_text = 'Faltam os seguintes campos: '
        for field in fields:
            message_text += f";{field}"
        return message_text

    def __create_message(self, message_text, message_type):
        code = 1
        msg_type = MessageType(f'Message {message_type}', message_type)
        if type(message_text) == list:
            message_text = self.__create_message_text_from_list(message_text)
        message = Message(code, message_text, msg_type)
        return message
