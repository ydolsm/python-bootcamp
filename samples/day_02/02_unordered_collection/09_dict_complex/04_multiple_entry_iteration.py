product_catalog = [
    {
   	    'name': 'Smartphone',
    	'description': 'Latest model smartphone.',
        'price': 999.99,
    	'stock': 25
    },
    {
    	'name': 'Wireless Headphones',
    	'description': 'Noise-canceling wireless headphones.',
    	'price': 199.99,
    	'stock': 50
    },
]

for entry in product_catalog:
    name = entry['name']
    description = entry['description']
    price = entry['price']
    stock = entry['stock']

    print(f"{name} ({price}) [{stock}] - {description}")