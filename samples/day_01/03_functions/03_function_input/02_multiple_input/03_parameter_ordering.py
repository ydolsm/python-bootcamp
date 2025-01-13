def calculate(num1, operator, num2):
    if operator == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operator== '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operator == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operator == '/':
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Invalid operator.")

calculate(1, "+", 2)