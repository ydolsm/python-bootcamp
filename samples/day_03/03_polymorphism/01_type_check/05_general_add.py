"""
Add a case for the following conditions
List and non-list (and vice versa)
Dict and non-dict (and vice versa)
Set and non-set (and vice versa)
"""


def add(x, y):
    if isinstance(x, (list, int)) and isinstance(y, (list, int)):
        return x + y
    elif isinstance(x, (set, dict)) and isinstance(y, (set, dict)):
        return x | y
    else:
        raise NotImplementedError()
