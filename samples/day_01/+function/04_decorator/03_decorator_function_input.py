def check_authentication(function):

    def wrapper(user):
        if user != "admin":
            print("Access denied!")
        else:
            return function(user)

    return wrapper


@check_authentication
def access_database(user):
    print("Accessing database...")
