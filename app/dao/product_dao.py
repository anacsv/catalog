from app.dao.base_dao_sql import BaseDao
from app.model.product import Product

class ProductDao(BaseDao):

    def __init__(self):
        super().__init__()

    # read
    def read(self, id: int = None):
        sql_select = f'SELECT id, name, description, price, gtin, product_condition_id, brand_id, shipping_country_id FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    # create
    def create(self, model: Product) -> str:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.name}'
                        ,'{model.description}'
                        ,'{model.price}'
                        ,'{model.gtin}'
                        ,'{model.product_condition_id}'
                        ,'{model.brand_id}'
                        ,'{model.shipping_country_id}'
                    )
                    ;'''
        return super().insert(sql_insert)

    # update    
    def update(self, model: Product) -> str:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    name = '{model.name}'
                    ,description = '{model.description}'
                    description = '{model.price}'
                    description = '{model.gtin}'
                    description = '{model.product_condition_id}'
                    description = '{model.brand_id}'
                    description = '{model.shipping_country_id}'
                    WHERE id = {model.id}; '''
        return super().update(sql_update)

    # delete
    def delete(self, id:int)->str:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        return super().delete(sql_delete)

    def __convert_data_object(self, data):
        if type(data) == list:
            products = []
            for item in data:
                product = self.__obj_converter(item)
                products.append(product)
            return products
        product = self.__obj_converter(data)
        return product

    def __obj_converter(self, item_tuple:tuple) -> Product:
        model = Product()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.description = item_tuple[2]
        return model
