#!/usr/bin/python2.7
# Licensed under MIT License

from ..model.items import Item
from ..model.items import ItemCollection

STORED_ITEMS = ItemCollection(items=[
  Item(title='Macbook Air', description='Super lightweight laptop', expiration='1337', price='1000$', item_id='1', owner='Max'),
  Item(title='Macbook Pro', description='Super fancy retina laptop', expiration='1337', price='1500$', item_id='2', owner='Tom'),
])

def listItems():
  return STORED_ITEMS

def getItem(item_id):
  for item in STORED_ITEMS.items:
      if item.item_id == item_id:
        return item
  raise endpoints.NotFoundException('Item %s not found.' %
                                            (item_id,))

if __name__ == '__main__':
  main()