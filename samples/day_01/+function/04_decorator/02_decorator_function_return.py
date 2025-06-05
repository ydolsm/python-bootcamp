def spaced(function):
    def wrapper():
        original = function()
        return "\n" + original + "\n"

    return wrapper


@spaced
def message():
    return "Good morning"


print(message())
