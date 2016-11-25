import re

text = "ababbababababbbbaaab"
pattern = "bb"

print (re.findall(pattern, text))
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print("Found %s at %d %d"%(text[s:e], s, e))
