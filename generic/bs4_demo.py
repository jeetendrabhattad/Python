html_doc = """
<html><head>
<title>The Dormouse's story</title>
</head>
<body>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link3">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#<p class="title"><b>The Dormouse's story</b></p>
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

soup.prettify()

print soup.title
# <title>The Dormouse's story</title>

print soup.title.name
# u'title'

print soup.title.string
# u'The Dormouse's story'

print soup.title.parent.name
# u'head'

#print soup.p
# <p class="title"><b>The Dormouse's story</b></p>

#print soup.p['class']
# u'title'

#print soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

#soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print "Magic"
print soup.find(id="link3")
print soup.findAll(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
