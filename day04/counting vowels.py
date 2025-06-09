def count_vowels():
    """Return the number of vowels in the given string"""

    letters = input("Enter text: ")

    letter_count = 0

    for letter in letters:
        vowels = ["a", "e", "i", "o", "u"]
        if letter in vowels:
            letter_count += 1
        #else:

    print (f"Vowel count: {letter_count}")

count_vowels()
