#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Item(messages.Message):
  """Item in the shop"""
  title       = messages.StringField(1)
  description = messages.StringField(2)
  expiration  = messages.StringField(3)
  price       = messages.StringField(4)
  item_id     = messages.StringField(5, required=True)
  owner       = messages.StringField(6)

class ItemDB(db.Model):
  title         = db.StringProperty()
  description   = db.StringProperty()
  expiration    = db.StringProperty()
  price         = db.StringProperty()
  item_id       = db.StringProperty(required=True)
  owner         = db.StringProperty()

class ItemCollection(messages.Message):
  """Collection of Items."""
  items = messages.MessageField(Item, 1, repeated=True)

if __name__ == '__main__':
    main()