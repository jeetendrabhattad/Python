import re
#import time

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'India', 'Country' ] ]
text = 'India is my Country.'

for regex in regexes:
    print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),
    if regex.search(text):
        print 'found a match!'
    else:
        print 'no match'
