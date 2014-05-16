#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Response(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.StringField(3, repeated=True) #repeated means array
