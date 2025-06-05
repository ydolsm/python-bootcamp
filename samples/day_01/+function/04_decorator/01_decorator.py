def decorator(function):
    def wrapper():
        print("Before the function runs...")
        function()
        print("After the function runs...")

    return wrapper


@decorator
def say_hello():
    print("Hello World")


say_hello()
