#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from ..model.items import Item
from ..model.items import ItemDB
from ..model.items import ItemCollection
from ..model.items import ResponseItem
from ..model.items import ResponseString

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

STORED_ITEMS = ItemCollection(items=[
  Item(title='Macbook Air', description='Super lightweight laptop', expiration='1337', price='1000$', item_id='1', owner='Max'),
  Item(title='Macbook Pro', description='Super fancy retina laptop', expiration='1337', price='1500$', item_id='2', owner='Tom'),
])

def listItems():
  itemList = []
  for item in ItemDB.query():
    itemList.append(itemDB_to_item(item))
  return ItemCollection(items=itemList)

def getItem(item_id):
  items = ItemDB.query(ItemDB.item_id == item_id)
  if items.count() > 1:
    raise endpoints.InternalServerErrorException('Multiple Items for %s found.' %
                                            (item_id,))
  elif items.count() == 1:
    return ResponseItem(msg='Item '+item_id, code='OK', data=itemDB_to_item(items.get()))
  raise endpoints.NotFoundException('Item %s not found.' %
                                            (item_id,))

def addItem(new_title='', new_description='', new_expiration='', new_price='', new_item_id='', new_owner=''):
  items = ItemDB.query(ItemDB.item_id == new_item_id)

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

def delItem(item_id):
  for item in ItemDB.query(ItemDB.item_id == item_id):
    item.key.delete()

  return ResponseString(msg="Item deleted succesfully",
                        code="OK",
                        data="")



def itemDB_to_item(item):
    return Item(title=item.title,
                description=item.description,
                expiration=item.expiration,
                price=item.price,
                item_id=item.item_id,
                owner=item.owner)
