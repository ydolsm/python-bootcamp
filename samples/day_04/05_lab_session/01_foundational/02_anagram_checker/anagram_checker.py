from collections import Counter



def anagram(first: str, second: str) -> bool:
    """Returns True if the first and second word are anagrams.

    Note: Listen and Silent are anagrams
    """
    print(Counter(first))
    print(Counter(second))

    print(Counter(first) == Counter(second))

first = input("Enter first word: ")
second = input("Enter second word: ")

anagram(first, second)