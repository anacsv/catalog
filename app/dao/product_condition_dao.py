from app.dao.base_dao import BaseDao
from app.model.product_condition import ProductCondition


class ProductConditionDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_condition'
        super().__init__(ProductCondition)

    # read
    def read(self, id: int = None):
        return super().read(id)

    # create
    def create(self, model: ProductCondition) -> ProductCondition:
        model.id = super().insert(model)
        return model

    # update
    def update(self, model: ProductCondition) -> ProductCondition:
        return super().update(model)

    # delete
    def delete(self, id: int) -> dict:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        rows = super().delete(sql_delete)
        if rows:
            return {'success': True, 'message': "deleted"}
        return {'success': False, 'message': "not found"}

    def __convert_data_object(self, data):
        if type(data) == list:
            conditions = []
            for item in data:
                condition = self.__obj_converter(item)
                conditions.append(condition)
            return conditions
        condition = self.__obj_converter(data)
        return condition

    def __obj_converter(self, item_tuple: tuple) -> ProductCondition:
        model = ProductCondition()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.description = item_tuple[2]
        return model
