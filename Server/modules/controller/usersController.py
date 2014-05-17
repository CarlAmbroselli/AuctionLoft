#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from ..model.users import *
from ..model.response import Response

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users


def listUsers():
  userList = []
  for user in UserDB.query():
    userList.append(userDB_to_user(user))
  return UserCollection(users=userList)

def getUser(user_id):
  users = UserDB.query(UserDB.user_id == user_id)
  if users.count() > 1:
    raise endpoints.InternalServerErrorException('Multiple Users for %s found.' %
                                            (user_id,))
  elif users.count() == 1:
    return Response(msg='User '+user_id, code='OK', data=[str(userDB_to_user(users.get()))])

  raise endpoints.NotFoundException('User %s not found.' %
                                            (user_id,))


def addUser(new_user_id='', new_email='', new_name='', new_description='', new_image_url='', new_tag='', new_disabled=''):
  response = Response(msg="Unknown Error", code="ERROR", data=[])
  users = UserDB.query(UserDB.user_id == new_user_id)

  if users.count() >= 1:
    return Response(msg="User with user_id "+new_user_id+" already exists!", code="ERROR", data=[])

  user = UserDB(user_id=new_user_id,
                email=new_email,
                name=new_name,
                description=new_description,
                image_url=new_image_url,
                tag=new_tag,
                disabled=new_disabled)
  user.put()
  response = Response(msg="User "+new_user_id+" added succesfully", code="OK", data=[str(userDB_to_user(user))])

  return response

def delUser(user_id):
  for user in UserDB.query(UserDB.user_id == user_id):
    user.key.delete()

  return Response(msg="User "+user_id+" deleted succesfully",
                  code="OK",
                  data=[])

def modUser(user_id, email, name, description, image_url, tag, disabled):
  arguments = locals()
  user = UserDB.query(UserDB.user_id == user_id)
  if user.count() > 1:
    return Response(msg="Multiple Users with this ID exist",
                    code="OK",
                    data=[])

  muser = user.get()
  for key in arguments:
    if arguments[key] != None and hasattr(muser, key):
      setattr(muser, key, arguments[key])
  muser.put()

  return Response(msg="User "+user_id+" modified succesfully",
                  code="OK",
                  data=[])

def userDB_to_user(user):
    return User(user_id=user.user_id,
                email=user.email,
                name=user.name,
                description=user.description,
                image_url=user.image_url,
                tag=user.tag,
                disabled=user.disabled)
