import re

address = re.compile('([\w\.-]+)@([\w\.]+)\.(\w+)')

email_ids = ['first.last@example.com',
              'first.last+category@gmail.com',
              'valid-address@mail.example.com.org',
              'valid@example.foo',
              'www.naval.com@gmail.com'
              ]

for email_id in email_ids:
        print
        print 'Candidate:', email_id
        match = address.search(email_id)
        if match:
            print '  Matches'
            print match.groups()
        else:
            print '  No match'
