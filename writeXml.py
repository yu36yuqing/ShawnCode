from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import dump
from xml.etree.ElementTree import Comment
from xml.etree.ElementTree import tostring

## Writing the content to xml document
book = ElementTree()

purchaseorder = Element('PurchaseOrder')
book._setroot(purchaseorder)

SubElement(purchaseorder,  'account', {'refnum' : "2390094"})

item = Element("item", {'sku' : '33-993933', 'qty' : '4'})
purchaseorder.append(item)
print item.items()       # [('sku', '33-993933'), ('qty', '4')]
print item.attrib        # {'sku': '33-993933', 'qty': '4'}
print item.get('sku')    # 33-993933
SubElement(item, 'name').text = "Potato Smasher"
SubElement(item, 'description').text = "Smash Potatoes like never before."

#book.write('book.xml',"utf-8")

#print tostring(purchaseorder)

#import sys
#book.write(sys.stdout)

#dump(book)
## Displaying the content of the xml document
print purchaseorder.find('account')
print purchaseorder.find('account').get('refnum')
print purchaseorder.findall('account')[0].get('refnum')

print purchaseorder.find('item/name')
print purchaseorder.find('item/name').text

## How to use ElementTree([element,] [file])
## 1. From standard XML element, it becomes root element
print ElementTree(item).getroot().find('name').text
## 2. From XML file
print ElementTree(file='book.xml').getroot().find('item/description').text


## Create an iterator
for element in purchaseorder.getiterator():
    print element.tag

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem

if __name__=="__main__":
    dump(indent(purchaseorder))
    book.write('book.xml',"utf-8")