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



