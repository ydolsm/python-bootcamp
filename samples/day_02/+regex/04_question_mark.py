import re

text = "color colour"

# Matches 'color' or 'colour'
pattern = r"colou?r"
matches = re.findall(pattern, text)

print(matches)
