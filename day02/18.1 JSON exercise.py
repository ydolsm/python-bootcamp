# Create a list of dictionaries containing dummy purchase information, then save it in a JSON file

import json

purchase_entries = [
	{"Name": "Egg",   "Price": 10, "Description": "It's an egg."},
	{"Name": "Milk",  "Price": 50, "Description": "Fresh cow milk."},
	{"Name": "Bread", "Price": 35, "Description": "A whole loaf."},
	{"Name": "Apple", "Price": 30, "Description": "Fresh apple"},
	{"Name": "Rice",  "Price": 60, "Description": "A kilo of rice."},
]

#default indent is 4
with open('purchase_entries.json', 'w') as file:
    json.dump(purchase_entries, file, indent=4)

# Save purchase_entries as a Json file