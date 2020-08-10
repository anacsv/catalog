from flask import Flask

from app.dao.product_brand_dao import ProductBrandDao
from app.dao.product_dao import ProductDao


app = Flask(__name__)
pd = ProductDao()

pbd = ProductBrandDao()


@app.route('/')
def initial():
    return pd.read()[0].__dict__()

app.run(debug=True)

