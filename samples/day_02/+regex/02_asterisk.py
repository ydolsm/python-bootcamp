import re

text = "aaabc acd aaaa bc"

# Matches 'bc' preceded by zero or more 'a's
pattern = r"a*bc"
matches = re.findall(pattern, text)

print(matches)
