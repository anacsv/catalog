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

    def __convert_data_object(self, data):
        if type(data) == list:
            products = []
            for item in data:
                product = self.__obj_converter(item)
                products.append(product)
            return products
        product = self.__obj_converter(data)
        return product

    def __obj_converter(self, item_tuple:tuple) -> Product:
        model = Product()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.description = item_tuple[2]
        model.price = item_tuple[3]
        model.gtin = item_tuple[4]
        model.product_condition_id = item_tuple[5]
        model.brand_id = item_tuple[6]
        model.shipping_country_id = item_tuple[7]
        return model
