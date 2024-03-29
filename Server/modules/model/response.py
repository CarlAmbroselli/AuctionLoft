#!/usr/bin/python2.7
# Licensed under MIT License

from protorpc import messages
import datetime
from google.appengine.api import users

from items import *
from feedback import *
from users import *
from comms import *

#### Items
class ItemResponse(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.MessageField(Item, 3, repeated=True)


#### Feedback
class FeedbackResponse(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.MessageField(Feedback, 3, repeated=True)

#### User
class UserResponse(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.MessageField(User, 3, repeated=True) #repeated means array

#### Comm
class CommResponse(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.MessageField(Comm, 3, repeated=True) #repeated means array


#### Generic
class Response(messages.Message):
  """JSON Response in the shop"""
  msg       = messages.StringField(1, required=True)
  code      = messages.StringField(2, required=True)
  data      = messages.StringField(3, repeated=True)
