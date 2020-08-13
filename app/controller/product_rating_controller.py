from app.dao.product_rating_dao import ProductRatingDao
from flask import jsonify, request
from flask_restful import Resource

from app.model.product_rating import ProductRating

class ProductRatingController(Resource):
    def __init__(self):
        self.__dao = ProductRatingDao()

    def get(self, id=None):
        if id:
            return jsonify(self.__dao.read(id).to_dict())
        return jsonify([prod_rat.to_dict() for prod_rat in self.__dao.read()])


    def post(self):
        data = request.get_json()
        product_rating = ProductRating(**data)
        model = self.__dao.create(product_rating)
        return jsonify(model.to_dict())


    def put(self, id):
        data = request.get_json()
        product_rating = ProductRating(**data)
        product_rating.id = id
        message = self.__dao.update(product_rating)
        return jsonify(message)


    def delete(self, id):
        message = self.__dao.delete(id)
        return jsonify(message)