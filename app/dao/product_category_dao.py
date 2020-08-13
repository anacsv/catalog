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
