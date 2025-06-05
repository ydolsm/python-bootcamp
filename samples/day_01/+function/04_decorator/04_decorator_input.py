def repeat(n):
    def decorator(function):
        def wrapper(message):
            result = function(message)
            return result * n

        return wrapper

    return decorator


@repeat(3)
def greeting(message):
    return f"Hello, {message}! "


print(greeting("Jeff"))
