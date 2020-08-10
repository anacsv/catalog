from app.dao.base_dao import BaseDao
from app.model.product_brand import ProductBrand


class ProductBrandDao(BaseDao):

    def __init__(self):
        super().__init__()

    def read(self, id: int = None):
        sql_select = f'SELECT id, name, fullname FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    def __create_object(self, item_str: str) -> ProductBrand:
        product_brand = ProductBrand()
        obj_array = item_str.split(';')
        product_brand.id = obj_array[0]
        product_brand.name = obj_array[1]
        product_brand.fullname = obj_array[2]
        return product_brand


        