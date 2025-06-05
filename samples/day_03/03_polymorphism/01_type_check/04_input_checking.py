def add(x, y):
    if isinstance(x, (list, int)) and isinstance(y, (list, int)):
        return x + y
    elif isinstance(x, (set, dict)) and isinstance(y, (set, dict)):
        return x | y
    else:
        raise NotImplementedError()
