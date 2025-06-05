import re

text = "aaabc abc aaaa bc"

# Matches 'bc' preceded by one or more 'a's
pattern = r"a+bc"
matches = re.findall(pattern, text)

print(matches)
