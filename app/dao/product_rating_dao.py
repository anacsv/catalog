from app.dao.base_dao_sql import BaseDao
from app.model.product_rating import ProductRating

class ProductRatingDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_rating'
        super().__init__()

    #read
    def read(self, id: int = None):
        sql_select = f'SELECT id, score, status FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    #create
    def create(self, model: ProductRating) -> str:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.score}'
                        ,'{model.status}'
                    )
                    ;'''
        return super().insert(sql_insert)

    #update
    def update(self, model: ProductRating) -> str:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    
                    score = '{model.score}'
                    , status = '{model.status}'
                    WHERE id = {model.id}; '''
        return super().update(sql_update)

    #delete
    def delete(self, id:int)->str:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        return super().delete(sql_delete)

    def __convert_data_object(self, data):
        if type(data) == list:
            conditions = []
            for item in data:
                condition = self.__obj_converter(item)
                conditions.append(condition)
            return conditions
        condition = self.__obj_converter(data)
        return condition

    def __obj_converter(self, item_tuple:tuple) -> ProductRating:
        model = ProductRating()
        model.id = item_tuple[0]
        model.score = item_tuple[1]
        model.status = item_tuple[2]
        return model