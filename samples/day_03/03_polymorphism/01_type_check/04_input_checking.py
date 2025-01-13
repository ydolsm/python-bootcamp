def add_item(items, item):
	if isinstance(items, list):
		items.append(item)
	elif isinstance(items, set):
		items.add(item)
	elif isinstance(items, dict):
		items[item] = item
	else:
		raise NotImplementedError()