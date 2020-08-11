from app.dao.product_dao import ProductDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product import Product


class ProductController(Resource):
    def __init__(self):
        self.__dao = ProductDao()

    def get(self,id=None):
        if id:
            return jsonify(self.__dao.read().__dict__())
        return jsonify([p.__dict__() for p in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product = Product(**data)
        model = self.__dao.create(product)
        return (jsonify(model.__dict__()))

    def put(self, id):
        data = request.get_json()
        product = Product(**data)
        product.id = id
        message = self.__dao.update(product)
        return jsonify(message)

    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)