import datetime
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

#Getting a Database
db = client.foo

#Getting a Collection
collection = db.artist


artist = {
        #"_id": "59f92ad107b8062bc8f09164",
        "_create_at":  datetime.datetime.utcnow(),
        "_update_at":  datetime.datetime.utcnow(),
        "type": "artist",
        "origin": "mongodb",
        "name": "bar",
        "website": "www.foo.bar.com",
        "bio": "bio",
        "genres": [
            "dance pop",
            "latin",
            "pop",
            "pop rap"
        ],
        "influences": "influences",
        "band_members": None,
        "hometown": "hometown",
        "country": "country",
        "external_urls": {
            "facebook": "facecook_url",
            "youtube": "youtube_url"
            }
        }

#insert
collection.insert_one(artist)           
