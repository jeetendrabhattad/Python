import re
import time
pattern = 'this'
text = 'Does this text match the pattern?'

print time.time()
match = re.search(pattern, text)
print time.time()

print match

s = match.start()
e = match.end()

print ('Found "%s" in "%s" from %d to %d ("%s")' % \
            (match.re.pattern, match.string, s, e, text[s:e]))
