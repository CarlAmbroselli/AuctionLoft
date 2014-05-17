#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime

from google.appengine.ext import ndb
from google.appengine.api import users

class User(messages.Message):
  """User in the shop"""
  user_id      = messages.StringField(1, required=True)
  email        = messages.StringField(2)
  name         = messages.StringField(3)
  description  = messages.StringField(4)
  image_url    = messages.StringField(5)
  tag          = messages.StringField(6)
  disabled     = messages.StringField(7)

class UserDB(ndb.Model):
  user_id      = ndb.StringProperty(required=True)
  email        = ndb.StringProperty()
  name         = ndb.StringProperty()
  description  = ndb.StringProperty()
  image_url    = ndb.StringProperty()
  tag          = ndb.StringProperty()
  disabled     = ndb.StringProperty()

class UserCollection(messages.Message):
  """Collection of Users."""
  users = messages.MessageField(User, 1, repeated=True)
