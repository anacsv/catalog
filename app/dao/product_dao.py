from app.dao.base_dao import BaseDao
from app.model.product import Product

class ProductDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product'
        super().__init__(Product)

    # read
    def read(self, id: int = None):
        return super().read(id)

    # create
    def create(self, model: Product) -> Product:
         model.id = super().insert(model)
         return model

    # update    
    def update(self, model: Product) -> Product:
        return super().update(model)

    # delete
    def delete(self, id: int) -> dict:
        return super().delete(id)
