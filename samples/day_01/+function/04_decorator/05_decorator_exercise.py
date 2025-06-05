"""
Create a decorator to change the behavior of the following functions:

>>> Command: user input 1
You inputted user input 1

>>> User: user input 2
You inputted user input 2
"""


def get_command():
    return input("Command: ")


def get_user():
    return input("User: ")


get_command()
get_user()
