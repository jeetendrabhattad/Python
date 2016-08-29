import re

text = "ababbababababbbbaaab"
pattern = "bb"

print re.findall(pattern, text)
for match in re.findall(pattern, text):
    print("Found %s"%match)
