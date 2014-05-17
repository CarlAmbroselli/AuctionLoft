#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users

class Feedback(messages.Message):
  """Item in the shop"""
  feedback_id    = messages.StringField(1, required=True)
  author         = messages.StringField(2)
  rating         = messages.StringField(3)
  comment        = messages.StringField(4)
  item_id        = messages.StringField(5)
  seller_uid     = messages.StringField(6)
  transaction_id = messages.StringField(7)

class FeedbackDB(ndb.Model):
  feedback_id    = ndb.StringProperty(required=True)
  author         = ndb.StringProperty()
  rating         = ndb.StringProperty()
  comment        = ndb.StringProperty()
  item_id        = ndb.StringProperty()
  seller_uid     = ndb.StringProperty()
  transaction_id = ndb.StringProperty()
