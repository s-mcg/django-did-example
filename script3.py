import sys
import requests
import json
from jose import jwt
from jose import jws
from jose import jwk

if len(sys.argv) == 1:
  print('no token provided. exiting')
  sys.exit(1)
token = sys.argv[1]
url='http://127.0.0.1:8000/didservice/.well-known/did.json'

response = requests.get(url)

json_response = json.loads(response.text)

pub_key = json_response["authentication"][0]["publicKeyMultibase"]

result = jwt.decode(token, key=pub_key, subject='1234560123')
print(result)