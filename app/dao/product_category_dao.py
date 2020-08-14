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
        model.id = super().insert(model)
        return model

    # update
    def update(self, model: ProductCategory) -> ProductCategory:
        return super().update(model)

    # delete
    def delete(self, id: int) -> dict:
        return super().delete(id)
