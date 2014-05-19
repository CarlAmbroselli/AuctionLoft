#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users

class Comm(messages.Message):
  """Item in the shop"""
  comm_id      = messages.StringField(1, required=True)
  subject      = messages.StringField(2, )#, required=True)
  sender       = messages.StringField(3)  #uid of Sender
  receiver     = messages.StringField(4) #uid of receiver
  timestamp    = messages.StringField(5)
  content      = messages.StringField(6)
  item_id      = messages.StringField(7)
  item_title   = messages.StringField(8)
  price        = messages.StringField(9)

class CommDB(ndb.Model):
  comm_id      = ndb.StringProperty(required=True)
  subject      = ndb.StringProperty() #, required=True)
  sender       = ndb.StringProperty()  #uid of Sender
  receiver     = ndb.StringProperty() #uid of receiver
  timestamp    = ndb.StringProperty()
  content      = ndb.StringProperty()
  item_id      = ndb.StringProperty()
  item_title   = ndb.StringProperty()
  price        = ndb.StringProperty()
