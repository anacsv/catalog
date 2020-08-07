from app.dao.base_dao import BaseDao
from app.model.product import Product

class ProductDao(BaseDao):

    def __init__(self):
        super().__init__()

    def read(self, id: int = None):
        sql_select = f'SELECT id, name, description FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    def __create_object(self, item_str: str) -> Product:
        product = Product()
        obj_array = item_str.split(';')
        product.id = obj_array[0]
        product.name = obj_array[1]
        product.description = obj_array[2]
        product.fullname = obj_array[3]
        return product


        