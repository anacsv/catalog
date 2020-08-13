from app.dao.base_dao import BaseDao
from app.model.product_brand import ProductBrand


class ProductBrandDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_brand'
        super().__init__(ProductBrand)

    # read
    def read(self, id: int = None):
        return super().read(id)

        # create

    def create(self, model: ProductBrand) -> ProductBrand:
        model.id = super().insert(model)
        return model

        # update

    def update(self, model: ProductBrand) -> ProductBrand:
        return super().update(model)

    # delete
    def delete(self, id: int) -> dict:
        return super().delete(id)

    def __convert_data_object(self, data):
        if type(data) == list:
            brands = []
            for item in data:
                brand = self.__obj_converter(item)
                brands.append(brand)
            return brands
        brands = self.__obj_converter(data)
        return brands

    def __obj_converter(self, item_tuple: tuple) -> ProductBrand:
        model = ProductBrand()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.full_name = item_tuple[2]
        return model