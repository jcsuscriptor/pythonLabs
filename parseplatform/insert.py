import http.client
import json

connection = http.client.HTTPConnection('localhost',1337) #, 443)

headers = {
            'Content-type': 'application/json', 
            "X-Parse-Application-Id": "123", 
          }


artist = {
        #"_id": "59f92ad107b8062bc8f09164",
        #"_create_at":  datetime.datetime.utcnow(),
        #"_update_at":  datetime.datetime.utcnow(),
        "type": "artist",
        "origin": "parse.api",
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

json_artist = json.dumps(artist)

connection.request('POST', '/parse/classes/Artist', json_artist, headers)

response = connection.getresponse()
print(response.read().decode())

 