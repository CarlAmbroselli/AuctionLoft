#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
import json
import collections
from ..model.items import Item
from ..model.items import ItemDB
from ..model.response import *

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

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
    return ItemResponse(msg='Item '+item_id, code='OK', data=[itemDB_to_item(items.get())])
  return ItemResponse(msg='Item '+item_id + ' not found!', code='OK', data=[])

def addItem(item):
  response = ItemResponse(msg="Unknown Error", code="ERROR", data=[])
  items = ItemDB.query(ItemDB.item_id == item.item_id)

  if items.count() >= 1:
    return ItemResponse(msg="Item with item_id "+new_item_id+" already exists!", code="ERROR", data=[])

  new_item = ItemDB(title=item.title,
                description=item.description,
                expiration=item.expiration,
                price=item.price,
                item_id=item.item_id,
                owner=item.owner)
  new_item.put()
  response = ItemResponse(msg="Item "+item.item_id+" added succesfully", code="OK", data=[itemDB_to_item(new_item)])

  return response

def delItem(item_id):
  for item in ItemDB.query(ItemDB.item_id == item_id):
    item.key.delete()

  return Response(msg="Item "+item_id+" deleted succesfully",
                  code="OK",
                  data=[])

def modItem(item):
  response = ItemResponse(msg="Unknown Error", code="ERROR", data=[])
  items = ItemDB.query(ItemDB.item_id == item.item_id)
  if items.count() > 1:
    response.msg = 'Multiple Items for ' + item.item_id + ' found.'
    response.code = 'ERROR'
  elif items.count() == 1:
    mItem = items.get()
    for key in arguments:
      if arguments[key] != None and hasattr(mItem, key):
        setattr(mItem, key, arguments[key])
    mItem.put()
    return ItemResponse(msg='Item '+item.item_id, code='OK', data=[itemDB_to_item(mItem)])
  return ItemResponse(msg='Item '+item.item_id + ' not found!', code='OK', data=[])



def itemDB_to_item(item):
    return Item(title=item.title,
                description=item.description,
                expiration=item.expiration,
                price=item.price,
                item_id=item.item_id,
                owner=item.owner)
