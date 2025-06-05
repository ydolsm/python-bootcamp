import re

text = "aaab aaa aa a a aaaab a"

# Matches 'aa' or 'aaa'
pattern = r"a{2,3}"
matches = re.findall(pattern, text)

print(matches)