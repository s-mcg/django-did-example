from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("This is the index for the web service.")

def did_json(request):
  key_str = get_key_from_disk()
  json_obj = _get_base_json()
  json_obj["authentication"][0]["publicKeyMultibase"] = key_str
  json_str = json.dumps(json_obj)
  return HttpResponse(json_str, content_type="text/json")

def get_key_from_disk():
  contents = ''
  with open("../public-key.key", 'r', encoding = 'utf-8') as f:
    contents = f.read()
    f.close()
  return contents


def _get_base_json():
  json_str = """
  {
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",
  "authentication": [{
    
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "Ed25519VerificationKey2020",
    "controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "changeme"
  }]
  }"""
  return json.loads(json_str)