from app.dao.base_dao import BaseDao
from app.model.shipping_country import ShippingCountry

class ShippingCountryDao(BaseDao):

    def __init__(self):
        self.__table_name = 'shipping_country'
        super().__init__(ShippingCountry)

    #read
    def read(self, id: int = None):
        return super().read(id)

    #create
    def create(self, model: ShippingCountry) -> ShippingCountry:
        model.id = super().insert(model)
        return model

    #update
    def update(self, model: ShippingCountry) -> ShippingCountry:
        model = super().update(model)
        return model

    #delete
    def delete(self, id:int)->dict:
        return  super().delete(id)
