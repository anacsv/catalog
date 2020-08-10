from flask import Flask

from app.dao.product_dao import ProductDao
from app.dao.product_category_dao import ProductCategoryDao

app = Flask(__name__)
pd = ProductDao()
pcd = ProductCategoryDao()


@app.route('/')
def initial():
    return pd.read()[0].__dict__()


@app.route('/product-category/')
def product_category():
    return pcd.read()[0].__dict__()


app.run(debug=True)
