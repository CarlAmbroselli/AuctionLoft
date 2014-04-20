"""Imports for AppEngine"""
import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

"""Entity imports"""
from entities.items import Item
from entities.items import ItemCollection


package = 'packagename'

STORED_ITEMS = ItemCollection(items=[
    Item(title='Macbook Air', description='Super lightweight laptop', expiration='1337', price='1000$', item_id='1', owner='Max'),
    Item(title='Macbook Pro', description='Super fancy retina laptop', expiration='1337', price='1500$', item_id='2', owner='Tom'),
])

@endpoints.api(name='staging', version='v1')
class ServerApi(remote.Service):
    """##Server API v1.##"""

    """List items"""
    @endpoints.method(message_types.VoidMessage, ItemCollection,
                      path='items', http_method='GET',
                      name='items.listItems')
    def items_list(self, unused_request):
        return STORED_ITEMS

    """Get single item"""
    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.StringField(1, variant=messages.Variant.STRING))

    @endpoints.method(ID_RESOURCE, Item,
                      path='item/{id}', http_method='GET',
                      name='items.getItem')
    def items_get(self, request):
        for item in STORED_ITEMS.items:
            if item.item_id == request.id:
                return item
        raise endpoints.NotFoundException('Item %s not found.' %
                                              (request.id,))

APPLICATION = endpoints.api_server([ServerApi])