from app.dao.base_dao import BaseDao
from app.model.product_category import ProductCategory


class ProductCategoryDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_category'
        super().__init__(ProductCategory)

    # read
    def read(self, id: int = None):
        return super().read(id)

    # create
    def create(self, model: ProductCategory) -> ProductCategory:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.name}'
                        ,'{model.description}'
                    )
                    ;'''
        model.id = super().insert(sql_insert)
        return model

    # update
    def update(self, model: ProductCategory) -> dict:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    name = '{model.name}'
                    ,description = '{model.description}'
                    WHERE id = {model.id}; '''
        rows = super().update(sql_update)
        if rows:
            return model.to_dict()
        return {'success': False, 'message': "not affected"}

    # delete
    def delete(self, id: int) -> dict:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        rows = super().delete(sql_delete)
        if rows:
            return {'success': True, 'message': "deleted"}
        return {'success': False, 'message': "not found"}

    def __convert_data_object(self, data):
        if type(data) == list:
            categories = []
            for item in data:
                category = self.__obj_converter(item)
                categories.append(category)
            return categories
        category = self.__obj_converter(data)
        return category

    def __obj_converter(self, item_tuple: tuple) -> ProductCategory:
        model = ProductCategory()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.description = item_tuple[2]
        return model
