import re

text = 'abbaaababbbbaaaaa'

pattern = '(ab)+'

iterator = re.finditer(pattern, text)
#print len(list(iterator))

for match in iterator:
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e], s, e)
