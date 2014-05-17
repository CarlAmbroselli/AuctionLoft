#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
import json
import collections
from ..model.feedback import Feedback
from ..model.feedback import FeedbackDB
from ..model.response import *

import datetime
from google.appengine.ext import ndb
from google.appengine.api import users

def listFeedback():
  response = FeedbackResponse(msg="Unknown Error", code="ERROR", data=[])
  count = 0
  for feedback in FeedbackDB.query():
    response.data.append(feedbackDB_to_feedback(feedback))
    count += 1
  response.msg = "Found " + str(count) + " feedback entries!"
  response.code = "OK"
  return response

def getFeedback(feedback_id):
  response = FeedbackResponse(msg="Unknown Error", code="ERROR", data=[])
  feedbacks = FeedbackDB.query(FeedbackDB.feedback_id == feedback_id)
  if feedbacks.count() > 1:
    response.msg = 'Multiple Feedback entries for ' + feedback_id + ' found.'
    response.code = 'ERROR'
  elif feedbacks.count() == 1:
    return FeedbackResponse(msg='Feedback '+feedback_id, code='OK', data=[feedbackDB_to_feedback(feedbacks.get())])
  return FeedbackResponse(msg='Feedback '+feedback_id + ' not found!', code='OK', data=[])

def addFeedback(feedback):
  response = FeedbackResponse(msg="Unknown Error", code="ERROR", data=[])
  feedbacks = FeedbackDB.query(FeedbackDB.feedback_id == feedback.feedback_id)

  if feedbacks.count() >= 1:
    return FeedbackResponse(msg="Feedback with feedback_id "+new_feedback_id+" already exists!", code="ERROR", data=[])

  new_feedback = FeedbackDB(
        feedback_id    = feedback.feedback_id,
        author         = feedback.author,
        rating         = feedback.rating,
        comment        = feedback.comment,
        item_id        = feedback.item_id,
        seller_uid     = feedback.seller_uid,
        transaction_id = feedback.transaction_id)
  new_feedback.put()
  response = FeedbackResponse(msg="Feedback "+feedback.feedback_id+" added succesfully", code="OK", data=[feedbackDB_to_feedback(new_feedback)])

  return response

def delFeedback(feedback_id):
  for feedback in FeedbackDB.query(FeedbackDB.feedback_id == feedback_id):
    feedback.key.delete()

  return Response(msg="Feedback "+feedback_id+" deleted succesfully",
                  code="OK",
                  data=[])

def modFeedback(feedback):
  response = FeedbackResponse(msg="Unknown Error", code="ERROR", data=[])
  feedbacks = FeedbackDB.query(FeedbackDB.feedback_id == feedback.feedback_id)
  if feedbacks.count() > 1:
    response.msg = 'Multiple Feedbacks for ' + feedback.feedback_id + ' found.'
    response.code = 'ERROR'
  elif feedbacks.count() == 1:
    mFeedback = feedbacks.get()
    for key in arguments:
      if arguments[key] != None and hasattr(mFeedback, key):
        setattr(mFeedback, key, arguments[key])
    mFeedback.put()
    return FeedbackResponse(msg='Feedback '+feedback.feedback_id, code='OK', data=[feedbackDB_to_feedback(mFeedback)])
  return FeedbackResponse(msg='Feedback '+feedback.feedback_id + ' not found!', code='OK', data=[])



def feedbackDB_to_feedback(feedback):
    return Feedback(
        feedback_id    = feedback.feedback_id,
        author         = feedback.author,
        rating         = feedback.rating,
        comment        = feedback.comment,
        item_id        = feedback.item_id,
        seller_uid     = feedback.seller_uid,
        transaction_id = feedback.transaction_id)
