from app.dao.base_dao import BaseDao
from app.model.product_brand import ProductBrand


class ProductBrandDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_brand'
        super().__init__()
    # read
    def read(self, id: int = None):
        sql_select = f'SELECT id, name, full_name FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

        # create

    def create(self, model: ProductBrand) -> str:
        sql_insert = f'''INSERT INTO {self.__table_name}
                       VALUES
                       (
                           0
                           ,'{model.name}'
                           ,'{model.full_name}'
                       )
                       ;'''
        model.id = super().insert(sql_insert)
        return model

        # update

    def update(self, model: ProductBrand) -> str:
        sql_update = f'''UPDATE {self.__table_name} 
                       SET
                       name = '{model.name}'
                       ,full_name = '{model.full_name}'
                       WHERE id = {model.id}; '''
        rows = super().update(sql_update)
        if rows:
            return model.__dict__()
        return {'success': False, 'message': "not affected"}

    # delete
    def delete(self, id: int) -> dict:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        rows = super().delete(sql_delete)
        if rows:
            return {'success': True, 'message': "product_brand deleted"}
        return {'success': False, 'message': "not found"}

    def __convert_data_object(self, data):
        if type(data) == list:
            brands = []
            for item in data:
                brand = self.__obj_converter(item)
                brands.append(brand)
            return brands
        brands = self.__obj_converter(data)
        return brands

    def __obj_converter(self, item_tuple: tuple) -> ProductBrand:
        model = ProductBrand()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.full_name = item_tuple[2]
        return model