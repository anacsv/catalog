from app.dao.base_dao import BaseDao
from app.model.shipping_country import ShippingCountry

class ShippingCountryDao(BaseDao):

    def __init__(self):
        self.__table_name = 'shipping_country'
        super().__init__()

    #read
    def read(self, id: int = None):
        sql_select = f'SELECT id, name, imported FROM {self.__table_name}'
        if id:
            sql_select += f' WHERE id= {id} '

        data = super().read(sql_select)
        return self.__convert_data_object(data)

    #create
    def create(self, model: ShippingCountry) -> ShippingCountry:
        sql_insert = f'''INSERT INTO {self.__table_name}
                    VALUES
                    (
                        0
                        ,'{model.name}'
                        ,'{model.imported}'
                    )
                    ;'''
        model.id = super().insert(sql_insert)
        return model

    #update
    def update(self, model: ShippingCountry) -> ShippingCountry:
        sql_update = f'''UPDATE {self.__table_name} 
                    SET
                    name = '{model.name}'
                    , imported = '{model.imported}'
                    WHERE id = {model.id}; '''
        rows = super().update(sql_update)
        if rows:
            return model.__dict__()
        return {'success': False, 'message': "not affected"}

    #delete
    def delete(self, id:int)->dict:
        sql_delete = f'DELETE FROM {self.__table_name} WHERE id = {id}'
        rows = super().delete(sql_delete)
        if rows:
            return {'success': True, 'message': "shipping_country deleted"}
        return {'success': False, 'message': "not found"}

    def __convert_data_object(self, data):
        if type(data) == list:
            conditions = []
            for item in data:
                condition = self.__obj_converter(item)
                conditions.append(condition)
            return conditions
        condition = self.__obj_converter(data)
        return condition

    def __obj_converter(self, item_tuple:tuple) -> ShippingCountry:
        model = ShippingCountry()
        model.id = item_tuple[0]
        model.name = item_tuple[1]
        model.imported = item_tuple[2]
        return model