import requests

'''testando os produtos manualmente pelo terminal'''

def test_list_of_products():
    r = requests.get("http://127.0.0.1:8000/products")
    response = r.json()
    print(response)

test_list_of_products()