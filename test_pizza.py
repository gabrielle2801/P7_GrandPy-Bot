import requests

def get_pizzas(quantity):
    """Returns a list of pizza names."""
    products = []
    payload = {
        "action": "process",
        "json": 1,
        "tagtype_0": "categories",
        "tag_contains_0": "contains",
        "tag_0": "pizzas",
        "page_size": quantity if quantity < 1000 else 1000
    }
    response = requests.get(
        'https://fr.openfoodfacts.org/cgi/search.pl',
        params=payload
    )
    if response.status_code == 200:
        products = response.json()['products']

    return [
        product['product_name'] for product in products
        if 'product_name' in product
    ]


def test_get_pizzas_returns_correct_names(monkeypatch):
    product1, product2 = products = ['My product 1', 'My product 2']
    class MockRequestsGet:
        def __init__(self, url, params=None):
            self.status_code = 200
        def json(self):
            return {
                "products": [{"product_name": product} for product in products]
            }

    monkeypatch.setattr('requests.get', MockRequestsGet)

    assert get_pizzas(len(products)) == products
