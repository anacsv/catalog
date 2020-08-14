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
        return super().delete(id)
