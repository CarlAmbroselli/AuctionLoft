#!/usr/bin/python2.7
# Licensed under MIT License

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote
from modules.controller.itemsController import *

@endpoints.api(name='staging', version='v1')
class ServerApi(remote.Service):

  ID_RESOURCE = endpoints.ResourceContainer(
                  message_types.VoidMessage,
                  id=messages.StringField(1, variant=messages.Variant.STRING))

  @endpoints.method(message_types.VoidMessage, ItemCollection,
                    path='items', http_method='GET',
                    name='items.listItems')
  def items_list(self, unused_request):
      return listItems()

  @endpoints.method(ID_RESOURCE, Item,
                    path='item/{id}', http_method='GET',
                    name='items.getItem')
  def items_get(self, request):
      return getItem(request.id)

APPLICATION = endpoints.api_server([ServerApi])
