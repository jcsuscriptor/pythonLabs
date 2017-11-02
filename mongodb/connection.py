import datetime
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

#Getting a Database
db = client.foo

#Getting a Collection
collection = db.artist

# PyMongo uses datetime.datetime objects for representing dates and times in MongoDB documents.
# Because MongoDB assumes that dates and times are in UTC, 
# care should be taken to ensure that dates and times written to the database reflect UTC
post = {"author": "Mike",
       "text": "My first blog post!",
       "tags": ["mongodb", "python", "pymongo"],
       "date": datetime.datetime.utcnow()}


posts = db.posts
posts.insert_one(post)       