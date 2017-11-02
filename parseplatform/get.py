import json,http.client

connection = http.client.HTTPConnection('localhost',1337) #, 443)
connection.connect()

#HTTPConnection.request(method, url, body=None, headers={}, *, encode_chunked=False)
connection.request('GET', '/parse/classes/Artist', '', {
       "X-Parse-Application-Id": "123", 
     })

result = json.loads(connection.getresponse().read())

print (result)
 

