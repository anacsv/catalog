from app.dao.base_dao import BaseDao
from app.model.product_rating import ProductRating

class ProductRatingDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_rating'
        super().__init__(ProductRating)

    #read
    def read(self, id: int = None):
        return super().read(id)

    #create
    def create(self, model: ProductRating) -> ProductRating:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.score}'
                        ,'{model.status}'
                        ,'{model.person_id}'
                        ,'{model.product_id}'
                    )
                    ;'''
        model.id = super().insert(sql_insert)
        return model

    #update
    def update(self, model: ProductRating) -> ProductRating:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    score = '{model.score}'
                    , status = '{model.status}'
                    , person_id = '{model.person_id}'
                    , product_id = '{model.product_id}'
                    WHERE id = {model.id}; '''
        rows = super().update(sql_update)
        if rows:
            return model.__dict__()
        return {'success': False, 'message': "not affected"}

    #delete
    def delete(self, id:int)->dict:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        rows = super().delete(sql_delete)
        if rows:
            return {'success': True, 'message': "product_rating deleted"}
        return {'success': False, 'message': "not found"}

    def __convert_data_object(self, data):
        if type(data) == list:
            conditions = []
            for item in data:
                condition = self.__obj_converter(item)
                conditions.append(condition)
            return conditions
        conditions = self.__obj_converter(data)
        return conditions

    def __obj_converter(self, item_tuple:tuple) -> ProductRating:
        model = ProductRating()
        model.id = item_tuple[0]
        model.score = item_tuple[1]
        model.status = item_tuple[2]
        model.person_id = item_tuple[3]
        model.product_id = item_tuple[4]
        return model