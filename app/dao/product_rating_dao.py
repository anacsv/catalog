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
        return super().insert(model)

    #update
    def update(self, model: ProductRating) -> ProductRating:
        return super().update(model)

    #delete
    def delete(self, id:int)->dict:
        return super().delete(id)