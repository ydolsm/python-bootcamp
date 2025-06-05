def http_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case code if 400 <= code < 500:
            return "Client Error"
        case code if 500 <= code < 600:
            return "Server Error"
        case code:
            return f"Unknown Status - {code}"


user_code = int(input("Status code: "))
user_status = http_status(user_code)

print(user_status)
