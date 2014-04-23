#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from ..model.items import Item
from ..model.items import ItemDB
from ..model.items import ItemCollection

import datetime
from google.appengine.ext import db
from google.appengine.api import users

STORED_ITEMS = ItemCollection(items=[
  Item(title='Macbook Air', description='Super lightweight laptop', expiration='1337', price='1000$', item_id='1', owner='Max'),
  Item(title='Macbook Pro', description='Super fancy retina laptop', expiration='1337', price='1500$', item_id='2', owner='Tom'),
])

def listItems():
  items = db.GqlQuery("SELECT * FROM ItemDB")
  itemList = []
  for item in items:
    itemList.append(itemDB_to_item(item))
  return ItemCollection(items=itemList)

def getItem(item_id):
  items = db.GqlQuery("SELECT * FROM ItemDB WHERE item_id = :1",
                                item_id)
  if items.count() > 1:
    raise endpoints.InternalServerErrorException('Multiple Items for %s found.' %
                                            (item_id,))
  elif items.count() == 1:
    return itemDB_to_item(items.get())
  raise endpoints.NotFoundException('Item %s not found.' %
                                            (item_id,))

def addItem(new_title='', new_description='', new_expiration='', new_price='', new_item_id='', new_owner=''):
  items = db.GqlQuery("SELECT * FROM ItemDB WHERE item_id = :1",
                                new_item_id)
  if items.count() >= 1:
    raise endpoints.InternalServerErrorException('Item with item_id %s already exists!' %
                                            (new_item_id,))

  item = ItemDB(title=new_title, 
                description=new_description, 
                expiration=new_expiration, 
                price=new_price, 
                item_id=new_item_id, 
                owner=new_owner)
  item.put()
  return itemDB_to_item(item)


def itemDB_to_item(item):
    return Item(title=item.title, 
                description=item.description, 
                expiration=item.expiration, 
                price=item.price, 
                item_id=item.item_id, 
                owner=item.owner)

if __name__ == '__main__':
  main()