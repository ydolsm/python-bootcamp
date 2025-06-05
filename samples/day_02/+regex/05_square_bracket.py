import re

text = "cat bat rat mat"

# Matches 'cat' or 'bat'
pattern = r"[cb]at"
matches = re.findall(pattern, text)

print(matches)
