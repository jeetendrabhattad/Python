#!/usr/bin/python

#[A-Z][A-Za-z]+[a-z]

import re

def TestPatterns(text, patterns=[]):
    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print('Matching {}'.format(pattern))
        for match in re.finditer(pattern, text):
            s=match.start()
            e=match.end()
            print("{0} : {1} string={2}".format(s,e-1,text[s:e]))
    return

if __name__ == '__main__':
    '''
    TestPatterns('abbaaabbbbaaaaa', ['ab','ab*','ab+','ab?','ab{3}','ab{2,3}'])
    '''
    '''
    TestPatterns('abbaaab45bbbbaaaaa',[ '[ab]',    # either a or b
                                      'a[ab]+',  # a followed by one or more a or b
                                      'a[ab]+?', # a followed by one or more a or b, not greedy
                                    ]) 
    '''
    '''
    TestPatterns('This is some text -- with punctuation.',
                          [ '[^-. ]+',  # sequences without -, ., or space
                              ])
    '''
    '''
    TestPatterns('This is some text -- with punctuation.',
                          [ '[a-z]+',      # sequences of lower case letters
                            '[A-Z]+',      # sequences of upper case letters
                            '[a-zA-Z]+',   # sequences of lower or upper case letters
                            '[A-Z][a-z]+', # one upper case letter followed by lower case letters
                            '[A-Z][a-z]',  # one upper case letter followed by one lower case 
                            ])
    '''
    '''
    TestPatterns('a7bbbbbaaaaaaaab',
                          [ 'a.',   # a followed by any one character
                            'b.',   # b followed by any one character
                            'a.*b', # a followed by anything, ending in b
                            'a.*?b', # a followed by anything, ending in b
                            ])
    
    '''
    #'''
    TestPatterns('This is a prime #1 example!',
                          [ r'\d+', # sequence of digits
                            r'\D+', # sequence of non-digits
                            r'\s+', # sequence of whitespace
                            r'\S+', # sequence of non-whitespace
                            r'\w+', # alphanumeric characters
                            r'\W+', # non-alphanumeric
                            ])
    #'''
    '''
    TestPatterns(r'\d+ \D+ \s+ \S+ \w+ \W+',
                          [ r'\\d\+',
                            r'\\D\+',
                            r'\\s\+',
                            r'\\S\+',
                            r'\\w\+',
                            r'\\W\+',
                            ]) 
    
    '''
    '''
    TestPatterns('This is some atexta -- with punctuation.',
            [ r'^\w+',     # alphanumeric word at start of string
                r'\A\w+',    # alphanumeric word at start of string
                r'\w+\S*$',  # alphanumeric word at end of string, with optional punctuation
                r'\w+\S*\Z', # alphanumeric word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\w+t\B',    # 't', not start or end of word
                ])
    '''
    '''
    TestPatterns('abbaaabbbbaaaaa',
            [ 'a(ab)',    # 'a' followed by literal 'ab'
                'a(a*b*)',  # 'a' followed by 0-n 'a' and 0-n 'b'
                'a(ab)*',   # 'a' followed by 0-n 'ab'
                'a(ab)+',   # 'a' followed by 1-n 'ab'
                ])
    '''
