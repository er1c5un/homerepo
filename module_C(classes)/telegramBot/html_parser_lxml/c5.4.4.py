import lxml.html
from lxml import etree

tree = etree.parse('tag2.html', lxml.html.HTMLParser())

elements = tree.findall("/body/tag1/tag2")
print(elements)
for el in elements:
    print('el =', el.text)
