from flask import Flask

from app.dao.product_dao import ProductDao
from app.dao.product_category_dao import ProductCategoryDao
from app.dao.product_condition_dao import ProductConditionDao

app = Flask(__name__)
pd = ProductDao()
p_category_dao = ProductCategoryDao()
p_condition_dao = ProductConditionDao()


@app.route('/')
def initial():
    return pd.read()[0].__dict__()


@app.route('/product-category')
def product_category():
    return p_category_dao.read()[0].__dict__()


@app.route('/product-condition')
def product_condition():
    return p_condition_dao.read()[0].__dict__()


app.run(debug=True)
