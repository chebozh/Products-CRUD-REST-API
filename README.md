# Flask REST API CRUD

This is a REST API made to apply some of the things I've been learning recenly on building REST APIs with Python and Flask.

For this project I've used Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-JWT to make the API, which supports CRUD operations. 

The project's main data objects/resources are items with specific attributes like name, price, sizes, url, seller and the online stores selling these items. For example: running shoes.

I've deployed the project on Heroku (free tier). It's available at https://products-rest-api.herokuapp.com


# API endpoints:

#### Retrieve the item with the specified name 

```/item/<name> ``` (GET)
		
Example: 	
```
curl https://products-rest-api.herokuapp.com/item/sneaker%20nike%20air%20monarch
```


#### Add an item the database

```/item/<name> ``` (POST)

Required request data params: 
 `price=[float]`
 `item_url=[string]`
 `store_url=[string]`

Optional params:
`sizes=[string]`
 
 Example: 
 ```
curl --header "Content-Type: application/json" \
 --request POST \
 --data '{"price": 160.40,
	"sizes": ["41", "44"],
	"item_url": "https://www.adidas.es/zapatilla-ultraboost-19/B37704.html",
	"store_url": "www.adidas.es"}' https://products-rest-api.herokuapp.com/item/Adidas_Ultra_Boost
  ```
  

#### Create a new item, or update an existing one
    
```/item/<name> ``` (PUT)

Required request data params: 
 `price=[float]`
 `item_url=[string]`
 `store_url=[string]`

Optional params:
`sizes=[string]`
 
Example:
```
curl --header "Content-Type: application/json" \
 --request PUT \
 --data '{"price": 60.99,
	"sizes": ["41", "44"],
	"item_url": "https://www.adidas.es/zapatilla-ultraboost-19/B37704.html",
	"store_url": "www.adidas.es"}' https://products-rest-api.herokuapp.com/item/Adidas_Ultra_Boost
  ```  

  
 #### Delete an item - Authentication required
 
 ```/item/<name> ``` (DELETE)
 
 Required request header:
  `Authorization=[string]`

Example:

```
curl ---request DELETE  -H "Authorization: JWT <ACCESS_TOKEN>" https://products-rest-api.herokuapp.com/item/sneaker%20nike%20air%20monarch
```


#### Retrieve all items  
    
```/items ``` (GET)

Example:

```
curl https://products-rest-api.herokuapp.com/items
```

#### Retrieve a store
```/store/<name> ``` (GET)
  
Example:
```
curl https://products-rest-api.herokuapp.com/store/www.deichman.com
```


#### Add a store to the database.

```/store/<name> ``` (POST)

Example:

```
curl --request POST https://products-rest-api.herokuapp.com/store/NewStore
```


 #### Delete a store - Authentication required
 
 ```/store/<name> ``` (DELETE)
 
 
 Example:

```
curl ---request DELETE  -H "Authorization: JWT <ACCESS_TOKEN>" https://products-rest-api.herokuapp.com/store/NewStore
```


#### Retrieve all stores (including their associated items)

```/stores ``` (GET)

Example:

```
curl https://products-rest-api.herokuapp.com/stores
```


 #### Authenticate - Currently only one admin user.
 
```/auth``` (POST)

Example:

```
curl --header "Content-Type: application/json" --request POST --data '{"username":"xyz","password":"xyz"}' https://products-rest-api.herokuapp.com/auth
```


There is a sub-directory test_api, where I've added some sample data (scraped with Scrapy) to the databse, using the API.

