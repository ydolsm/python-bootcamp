"""
Word Match Counter

    1. Ask user for word to find (be careful of extra spaces on the left and right side of input)
    2. Ask user for filepath on text file to read
    3. Read text file contents and put in a variable
    4. Count the instance of the word:
        - Exact match: Number of exact matches
        - Incorrect case: Number of matches but the case is incorrect (some lower or uppercasing)
"""

def word_match_counter():

    word_to_find = input("Enter word to find: ")
    word_file = input("Enter text file to read: ")

    word_match_count = 0

    for word in word_file():
        with open(word_file, "r") as file:
            file_contents = file.read()

        if word_to_find in word_file:
            word_match_count += 1
        else




word_match_counter()