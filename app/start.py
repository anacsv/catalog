from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from app.controller.product_controller import ProductController
from app.controller.product_brand_controller import ProductBrandController
from app.controller.product_category_controller import ProductCategoryController
from app.controller.product_condition_controller import ProductConditionController
from app.controller.product_rating_controller import ProductRatingController
from app.controller.shipping_country_controller import ShippingCountryController

#command+d -> ctrl+g

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

@app.route('/')
def initial():
    return ' '

# ------------------------------------------ Product
api.add_resource(ProductController, '/api/product/', endpoint='products')
api.add_resource(ProductController, '/api/product/<int:id>', endpoint='product')
# ------------------------------------------ Product finish

# ------------------------------------------ Product Brand
api.add_resource(ProductBrandController, '/api/product-brand/', '/api/product-brand/<int:id>', endpoint='product-brands')
# ------------------------------------------ Product Brand finish

# ------------------------------------------ Product Rating init
api.add_resource(ProductRatingController, '/api/product-rating/', endpoint='product-ratings')
api.add_resource(ProductRatingController, '/api/product-rating/<int:id>', endpoint='product-rating')
# ------------------------------------------ Product Rating finish


# ------------------------------------------ Shipping Country init
api.add_resource(ShippingCountryController, '/api/shipping-country/', endpoint='shipping-countries')
api.add_resource(ShippingCountryController, '/api/shipping-country/<int:id>', endpoint='shipping-country')
# ------------------------------------------ Shipping Country finish


api.add_resource(ProductCategoryController, '/api/product-category/', endpoint='product-categories')
api.add_resource(ProductCategoryController, '/api/product-category/<int:id>/', endpoint='product-category')

api.add_resource(ProductConditionController, '/api/product-condition/', endpoint='product-conditions')
api.add_resource(ProductConditionController, '/api/product-condition/<int:id>/', endpoint='product-condition')

app.run(debug=True)
