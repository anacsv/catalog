from app.dao.shipping_country_dao import ShippingCountryDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.shipping_country import ShippingCountry

class ShippingCountryController(Resource):
    def __init__(self):
        self.__dao = ShippingCountryDao()

    def get(self, id=None):
        if id:
            return jsonify(self.__dao.read(id).to_dict())
        return jsonify([ship_count.to_dict() for ship_count in self.__dao.read()])


    def post(self):
        data = request.get_json()
        shipping_country = ShippingCountry(**data)
        model = self.__dao.create(shipping_country)
        return jsonify(model.to_dict())


    def put(self, id):
        data = request.get_json()
        shipping_country = ShippingCountry(**data)
        shipping_country.id = id
        model = self.__dao.update(shipping_country)
        return jsonify(model.to_dict())


    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)