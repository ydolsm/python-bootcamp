import json
with open('purchase_entries.json', 'r') as file:
    purchase_entries = json.load(file)
print(purchase_entries)