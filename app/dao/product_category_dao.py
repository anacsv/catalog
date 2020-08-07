from app.dao.base_dao_sql import BaseDao

class ProductCategoryDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_category'
        super().__init__()
