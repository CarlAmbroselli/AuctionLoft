#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
import json
import collections
from ..model.comms import Comm
from ..model.comms import CommDB
from ..model.response import *

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

def listComm():
  response = CommResponse(msg="Unknown Error", code="ERROR", data=[])
  count = 0
  for comm in CommDB.query():
    response.data.append(commDB_to_Comm(comm))
    count += 1
  response.msg = "Found " + str(count) + " comms!"
  response.code = "OK"
  return response

def getComm(comm_id):
  response = CommResponse(msg="Unknown Error", code="ERROR", data=[])
  comms = CommDB.query(CommDB.comm_id == comm_id)
  if comms.count() > 1:
    response.msg = 'Multiple Items for ' + comm_id + ' found.'
    response.code = 'ERROR'
  elif comms.count() == 1:
    return CommResponse(msg='Item '+comm_id, code='OK', data=[commDB_to_Comm(comms.get())])
  return CommResponse(msg='Item '+comm_id + ' not found!', code='OK', data=[])

def addComm(comm):
  response = CommResponse(msg="Unknown Error", code="ERROR", data=[])
  comms = CommDB.query(CommDB.comm_id == comm.comm_id)

  if comms.count() >= 1:
    return CommResponse(msg="Item with comm_id "+comm.comm_id+" already exists!", code="ERROR", data=[])

  new_comm = CommDB(comm_id=comm.comm_id,
                    subject=comm.subject,
                    sender=comm.sender,
                    receiver=comm.receiver,
                    timestamp=comm.timestamp,
                    content=comm.content,
                    item_id=comm.item_id,
                    item_title=comm.item_title,
                    price=comm.price)
  new_comm.put()
  response = CommResponse(msg="Item "+item.comm_id+" added succesfully", code="OK", data=[commDB_to_Comm(new_comm)])

  return response

def delComm(comm_id):
  for comm in CommDB.query(CommDB.comm_id == comm_id):
    comm.key.delete()

  return Response(msg="Item "+comm_id+" deleted succesfully",
                  code="OK",
                  data=[])


def commDB_to_Comm(comm):
    return Comm(comm_id   =comm.comm_id,
                subject   =comm.subject,
                sender    =comm.sender,
                receiver  =comm.receiver,
                timestamp =comm.timestamp,
                content   =comm.content,
                item_id   =comm.item_id,
                item_title=comm.item_title,
                price=comm.price)
