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