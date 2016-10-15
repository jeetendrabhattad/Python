from xml.etree import ElementTree
import logging

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)
    #print tree

for node in tree.iter():
    print node.tag, node.attrib

logging.warning('Watch out!')
logging.error('It is an error!')
