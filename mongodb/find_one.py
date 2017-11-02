import datetime
import pprint
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
        "origin": "demo",
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
artist_id = collection.insert_one(artist).inserted_id

#get
artist_get = collection.find_one({"_id": artist_id})
pprint.pprint(artist_get)


#get insert from c#
pprint.pprint("--------------------------")
pprint.pprint("Get document insert from c#:")
pprint.pprint("--------------------------")
id = "59f9366b07b8082bc8109b50"
artist_insert_c = collection.find_one({"_id": id})
pprint.pprint(artist_insert_c)
