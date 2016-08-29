import re

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print 'Text        :', repr(text)
print 'Pattern     :', pattern
print 'No newlines :', no_newlines.findall(text)
print 'Dotall      :', dotall.findall(text)

