from collections import Counter, deque

# Counter
print("Using Counter:")
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)
print()

# deque
print("Using deque:")
d = deque(["first", "second", "third"])
d.append("fourth")
d.appendleft("zeroth")
print(d)
d.pop()
d.popleft()
print(d)
