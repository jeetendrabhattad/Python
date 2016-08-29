import re

text = 'aaSSSabbaaabbbb ,,, aaaaa234234adsasdas'
text = '1212'
pattern = '[a-zA-Z]+'

m = re.match(pattern, text)
if m:
    s = m.start()
    e = m.end()
    print s, e, text[s:]
else:
    print ("Match nt found")

for match in re.findall(pattern, text):
        print 'Found "%s"' % match
