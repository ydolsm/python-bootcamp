import re

text = "cat bat hat ctt"

# Matches any three-character word starting with 'c' and ending with 't'
pattern = r"c.t"
matches = re.findall(pattern, text)

print(matches)
