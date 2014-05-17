#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from modules.controller.itemsController import *
from modules.controller.usersController import *
from modules.controller.feedbackController import *
from modules.model.response import *

@endpoints.api(name='staging', version='v1')
class ServerApi(remote.Service):

################################################################################
##############################   ITEM API ######################################
################################################################################

  ID_RESOURCE = endpoints.ResourceContainer(
                  message_types.VoidMessage,
                  id=messages.StringField(1, variant=messages.Variant.STRING))

  @endpoints.method(message_types.VoidMessage, ItemResponse,
                    path='items', http_method='GET',
                    name='items.listItems')
  def items_list(self, unused_request):
      return listItems()

  @endpoints.method(ID_RESOURCE, ItemResponse,
                    path='item/{id}', http_method='GET',
                    name='items.getItem')
  def items_get(self, request):
      return getItem(request.id)

  ITEM_RESOURCE = endpoints.ResourceContainer(Item)

  @endpoints.method(ITEM_RESOURCE, ItemResponse,
                  path='item/add', http_method='POST',
                  name='items.addItem')
  def items_add(self, request):
      return addItem(request)

  @endpoints.method(ID_RESOURCE, Response,
                    path='item/del/{id}', http_method='POST',
                    name='items.delItem')
  def items_del(self, request):
      return delItem(request.id)

  @endpoints.method(ITEM_RESOURCE, ItemResponse,
                   path='item/mod', http_method='POST',
                   name='items.modItems')
  def items_mod(self, request):
     return modItem(request)


################################################################################
##############################   USER API ######################################
################################################################################

  @endpoints.method(message_types.VoidMessage, UserResponse,
                    path='users', http_method='GET',
                    name='users.listUsers')
  def users_list(self, unused_request):
      return listUsers()

  @endpoints.method(ID_RESOURCE, UserResponse,
                    path='user/{id}', http_method='GET',
                    name='users.getUser')
  def users_get(self, request):
      return getUser(request.id)

  USER_RESOURCE = endpoints.ResourceContainer(User)

  @endpoints.method(USER_RESOURCE, UserResponse,
                  path='user/add', http_method='POST',
                  name='users.addUser')
  def users_add(self, request):
      return addUser(new_user_id=request.user_id,
                     new_email=request.email,
                     new_name=request.name,
                     new_description=request.description,
                     new_image_url=request.image_url,
                     new_tag=request.tag,
                     new_disabled=request.disabled)

  @endpoints.method(ID_RESOURCE, UserResponse,
                    path='del/{id}', http_method='POST',
                    name='users.delUser')
  def items_del(self, request):
      return delUser(request.id)

  @endpoints.method(USER_RESOURCE, UserResponse,
                    path='user/mod', http_method='POST',
                    name='users.modUsers')
  def users_mod(self, request):
      return modUser(user_id=request.user_id,
                     email=request.email,
                     name=request.name,
                     description=request.description,
                     image_url=request.image_url,
                     tag=request.tag,
                     disabled=request.disabled)

################################################################################
##########################   FEEDBACK API ######################################
################################################################################

  @endpoints.method(message_types.VoidMessage, FeedbackResponse,
                    path='feedbacks', http_method='GET',
                    name='feedback.listFeedbacks')
  def feedback_list(self, unused_request):
      return listFeedback()

  @endpoints.method(ID_RESOURCE, FeedbackResponse,
                    path='feedbacks/{id}', http_method='GET',
                    name='feedbacks.getFeedback')
  def feedback_get(self, request):
      return getFeedback(request.id)

  FEEDBACK_RESOURCE = endpoints.ResourceContainer(Feedback)

  @endpoints.method(FEEDBACK_RESOURCE, FeedbackResponse,
                  path='feedbacks/add', http_method='POST',
                  name='feedbacks.addFeedback')
  def feedback_add(self, request):
      return addFeedback(request)

  @endpoints.method(ID_RESOURCE, Response,
                    path='feedbacks/del/{id}', http_method='POST',
                    name='feedbacks.delFeedback')
  def feedback_del(self, request):
      return delFeedback(request.id)

  @endpoints.method(ITEM_RESOURCE, FeedbackResponse,
                   path='feedbacks/mod', http_method='POST',
                   name='feedbacks.modFeedbacks')
  def feedback_mod(self, request):
     return modFeedback(request)


APPLICATION = endpoints.api_server([ServerApi])
