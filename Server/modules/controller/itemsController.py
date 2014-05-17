#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
import json
import collections
from ..model.items import Item
from ..model.items import ItemDB
from ..model.items import ItemCollection
from ..model.response import *

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

STORED_ITEMS = ItemCollection(items=[
  Item(title='Macbook Air', description='Super lightweight laptop', expiration='1337', price='1000$', item_id='1', owner='Max'),
  Item(title='Macbook Pro', description='Super fancy retina laptop', expiration='1337', price='1500$', item_id='2', owner='Tom'),
])

def listItems():
  response = ItemResponse(msg="Unknown Error", code="ERROR", data=[])
  count = 0
  for item in ItemDB.query():
    response.data.append(itemDB_to_item(item))
    count += 1
  response.msg = "Found " + str(count) + " items!"
  response.code = "OK"
  return response

def getItem(item_id):
  response = ItemResponse(msg="Unknown Error", code="ERROR", data=[])
  items = ItemDB.query(ItemDB.item_id == item_id)
  if items.count() > 1:
    response.msg = 'Multiple Items for ' + item_id + ' found.'
    response.code = 'ERROR'
  elif items.count() == 1:
    return Response(msg='Item '+item_id, code='OK', data=itemDB_to_item(items.get()))
  return Response(msg='Item '+item_id + ' not found!', code='OK', data=[])

def addItem(new_title='', new_description='', new_expiration='', new_price='', new_item_id='', new_owner=''):
  response = ItemResponse(msg="Unknown Error", code="ERROR", data=[])
  items = ItemDB.query(ItemDB.item_id == new_item_id)

  if items.count() >= 1:
    return ItemResponse(msg="Item with item_id "+new_item_id+" already exists!", code="ERROR", data=[])

  item = ItemDB(title=new_title,
                description=new_description,
                expiration=new_expiration,
                price=new_price,
                item_id=new_item_id,
                owner=new_owner)
  item.put()
  response = ItemResponse(msg="Item "+new_item_id+" added succesfully", code="OK", data=[itemDB_to_item(item)])

  return response

def delItem(item_id):
  for item in ItemDB.query(ItemDB.item_id == item_id):
    item.key.delete()

  return Response(msg="Item "+item_id+" deleted succesfully",
                  code="OK",
                  data=[])



def itemDB_to_item(item):
    return Item(title=item.title,
                description=item.description,
                expiration=item.expiration,
                price=item.price,
                item_id=item.item_id,
                owner=item.owner)
