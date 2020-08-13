from app.dao.product_condition_dao import ProductConditionDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_condition import ProductCondition


class ProductConditionController(Resource):

    def __init__(self):
        self.__dao = ProductConditionDao()

    def get(self, id: int = None):
        if id:
            return jsonify(self.__dao.read(id).to_dict())
        return jsonify([p_condition.to_dict() for p_condition in self.__dao.read()])

    def post(self):
        data = request.get_json()
        product_condition = ProductCondition(**data)
        model = self.__dao.create(product_condition)
        return jsonify(model.to_dict())

    def put(self, id):
        data = request.get_json()
        product_condition = ProductCondition(**data)
        product_condition.id = id
        message = self.__dao.update(product_condition)
        return jsonify(message)

    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)
