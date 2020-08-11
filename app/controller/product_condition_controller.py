from app.dao.product_condition_dao import ProductConditionDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_condition import ProductCondition


class ProductConditionController(Resource):

    def __init__(self):
        self.__dao = ProductConditionDao()

    def get(self, id: int = None):
        if id:
            return jsonify(self.__dao.read(id).__dict__())
        return jsonify([p_condition.__dict__() for p_condition in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product_condition = ProductCondition(**data)
        model = self.__dao.create(product_condition)
        return jsonify(model.__dict__())

    def put(self):
        pass

    def delete(self):
        pass
