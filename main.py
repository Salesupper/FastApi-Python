from fastapi import FastAPI
from product import Product
from json_db import JsonDB


app = FastAPI()

produtoDB = JsonDB(path='.\data\products.json')

@app.get('/products')
def get_products():
    products = produtoDB.read()
    return { "products" : products }

@app.post('/products')
def create_products(product: Product):
    produtoDB.insert(product)
    return { "status" : "inserted" }






