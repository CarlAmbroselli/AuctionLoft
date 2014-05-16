#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from modules.controller.itemsController import *
from modules.model.response import *

class PostMessage(messages.Message):
  title       = messages.StringField(1)
  description = messages.StringField(2)
  expiration  = messages.StringField(3)
  price       = messages.StringField(4)
  item_id     = messages.StringField(5)
  owner       = messages.StringField(6)

POST_RESOURCE = endpoints.ResourceContainer(PostMessage)

@endpoints.api(name='staging', version='v1')
class ServerApi(remote.Service):

  ID_RESOURCE = endpoints.ResourceContainer(
                  message_types.VoidMessage,
                  id=messages.StringField(1, variant=messages.Variant.STRING))

  @endpoints.method(message_types.VoidMessage, Response,
                    path='items', http_method='GET',
                    name='items.listItems')
  def items_list(self, unused_request):
      return listItems()

  @endpoints.method(ID_RESOURCE, Response,
                    path='item/{id}', http_method='GET',
                    name='items.getItem')
  def items_get(self, request):
      return getItem(request.id)

  ITEM_RESOURCE = endpoints.ResourceContainer(
        Item#,
        #times=messages.IntegerField(2, variant=messages.Variant.INT32,
        #                            required=True)
        )

  @endpoints.method(ITEM_RESOURCE, Response,
                  path='item/add', http_method='POST',
                  name='items.addItem')
  def items_add(self, request):
      return addItem(new_title=request.title,
                     new_description=request.description,
                     new_expiration=request.expiration,
                     new_price=request.price,
                     new_item_id=request.item_id,
                     new_owner=request.owner)

  @endpoints.method(ID_RESOURCE, Response,
                    path='del/{id}', http_method='POST',
                    name='items.delItem')
  def items_del(self, request):
      return delItem(request.id)

#  @endpoints.method(Item, Item,
#                    path='item/mod', http_method='POST',
#                    name='items.modItems')
#  def items_mod(self, request):
#      return modItem()


APPLICATION = endpoints.api_server([ServerApi])
