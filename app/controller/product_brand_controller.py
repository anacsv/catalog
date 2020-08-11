from app.dao.product_brand_dao import ProductBrandDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_brand import ProductBrand


class ProductBrandController(Resource):
    def __init__(self):
        self.__dao = ProductBrandDao()

    def get(self,id=None):
        if id:
            return jsonify(self.__dao.read(id).__dict__())
        return jsonify([p_brand.__dict__() for p_brand in self.__dao.read(id)])

    def post(self):
        data = request.get_json()
        product_brand = ProductBrand(**data)
        model = self.__dao.create(product_brand)
        return (jsonify(model.__dict__()))

    def put(self, id):
        data = request.get_json()
        product_brand = ProductBrand(**data)
        product_brand.id = id
        message = self.__dao.update(product_brand)
        return jsonify(message)

    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)