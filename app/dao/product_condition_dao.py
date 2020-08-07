from app.dao.base_dao_sql import BaseDao

class ProductConditionDao(BaseDao):

    def __init__(self):
        self.__table_name = 'product_condition'
        super().__init__()
