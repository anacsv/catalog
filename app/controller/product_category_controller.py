from app.dao.product_category_dao import ProductCategoryDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_category import ProductCategory


class ProductCategoryController(Resource):

    def __init__(self):
        self.__dao = ProductCategoryDao()

    def get(self, id: int = None):
        if id:
            return jsonify(self.__dao.read(id).__dict__())
        return jsonify([p_category.__dict__() for p_category in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product_category = ProductCategory(**data)
        model = self.__dao.create(product_category)
        return jsonify(model.__dict__())

    def update(self):
        pass

    def delete(self):
        pass
