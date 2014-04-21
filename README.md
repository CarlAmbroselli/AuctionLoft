#AuctionLoft

Python Backend and Server for Secure Coding Seminar 2014

AppEngine Instance running on: [https://auctionloft.appspot.com](https://auctionloft.appspot.com)

##Endpoints

###List Items
|Path    | Method | Params | Authorization |
|:-------|:-------|:-------|:--------------|
|/items  |GET     |none    |no 			   |
 

#####Request:
~~~
GET https://auctionloft.appspot.com/_ah/api/staging/v1/items
~~~

#####Response:
~~~
{
 "items": [
  {
   "description": "Super lightweight laptop",
   "title": "Macbook Air",
   "price": "1000$",
   "owner": "Max",
   "expiration": "1337",
   "item_id": "1",
   "kind": "staging#itemsItem"
  },
  {
   "description": "Super fancy retina laptop",
   "title": "Macbook Pro",
   "price": "1500$",
   "owner": "Tom",
   "expiration": "1337",
   "item_id": "2",
   "kind": "staging#itemsItem"
  }
 ],
 "kind": "staging#items",
 "etag": "\"gXhqy01Wkwh3eRtwUqEtA2ewiXg/hsIf2C-jZtYE9HNhxM1rCoDFl8Q\""
}
~~~

###Get Item
|Path    	 | Method | Params | Authorization |
|:-----------|:-------|:-------|:--------------|
|/item/{id}  |GET     |none    |no 			   |
 

#####Request:
~~~
GET https://auctionloft.appspot.com/_ah/api/staging/v1/item/1
~~~

#####Response:
~~~
{
 "description": "Super lightweight laptop",
 "expiration": "1337",
 "item_id": "1",
 "owner": "Max",
 "price": "1000$",
 "title": "Macbook Air"
}
~~~
