from app.dao.product_category_dao import ProductCategoryDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_category import ProductCategory


class ProductCategoryController(Resource):

    def __init__(self):
        self.__dao = ProductCategoryDao()

    def get(self, id: int = None):
        if id:
            return jsonify(self.__dao.read(id).to_dict())
        return jsonify([p_category.to_dict() for p_category in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product_category = ProductCategory(**data)
        message = self.__dao.create(product_category)
        return jsonify(message)

    def put(self, id):
        data = request.get_json()
        product_category = ProductCategory(**data)
        product_category.id = id
        message = self.__dao.update(product_category)
        return jsonify(message)

    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)
