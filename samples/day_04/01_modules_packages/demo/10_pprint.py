import pprint

# Create a nested dictionary
data = {
    'person': {
        'name': 'Alice',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'New York',
            'postal_code': '10001'
        }
    },
    'job': 'Engineer'
}

# Normal print the dictionary
print(data)
print()

# Pretty-print the dictionary
pprint.pprint(data)
