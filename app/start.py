from flask import Flask, jsonify, request
from flask_restful import Api


from app.controller.product_brand_controller import ProductBrandController
from app.controller.product_category_controller import ProductCategoryController
from app.controller.product_condition_controller import ProductConditionController
from app.controller.product_rating_controller import ProductRatingController
from app.controller.shipping_country_controller import ShippingCountryController

from app.dao.product_dao import ProductDao

#command+d -> ctrl+g

app = Flask(__name__)
api = Api(app)

p_dao = ProductDao()

# ------------------------------------------ Product Brand
api.add_resource(ProductBrandController, '/api/product-brand/', endpoint='product-brands')
api.add_resource(ProductBrandController, '/api/product-brand/<int:id>', endpoint='product-brand')
# ------------------------------------------ Product Brand finish


# ------------------------------------------ Product Rating init
api.add_resource(ProductRatingController, '/api/product-rating/', endpoint='product-ratings')
api.add_resource(ProductRatingController, '/api/product-rating/<int:id>', endpoint='product-rating')
# ------------------------------------------ Product Rating finish


# ------------------------------------------ Shipping Country init
api.add_resource(ShippingCountryController, '/api/shipping-country/', endpoint='shipping-countries')
api.add_resource(ShippingCountryController, '/api/shipping-country/<int:id>', endpoint='shipping-country')
# ------------------------------------------ Shipping Country finish

@app.route('/')
def initial():
    return ' '


@app.route('/product', methods=['GET'])
def product():
    return jsonify([p.__dict__() for p in p_dao.read()]), 200


@app.route('/product', methods=['POST'])
def product_create():
    data = request.get_json()
    product = Product(**data)
    model = p_dao.create(product)
    return (jsonify(model.__dict__())), 201


@app.route('/product', methods=['DELETE'])
def product_delete():
    id = request.args.get('id')
    message = p_dao.delete(id)
    return jsonify(message), 200

@app.route('/product', methods=['PUT'])
def product_update():
    data = request.get_json()
    product = Product(**data)
    message = p_dao.update(product)
    return jsonify(message), 200


api.add_resource(ProductCategoryController, '/api/product-category/', endpoint='product-categories')
api.add_resource(ProductCategoryController, '/api/product-category/<int:id>/', endpoint='product-category')


api.add_resource(ProductConditionController, '/api/product-condition/', endpoint='product-conditions')
api.add_resource(ProductConditionController, '/api/product-condition/<int:id>/', endpoint='product-condition')


app.run(debug=True)
