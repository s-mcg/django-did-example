from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):
    return HttpResponse("This is the index for the web service.")

def did_json(request):
  json_obj = _get_base_json()
  json_str = json.dumps(json_obj)
  return HttpResponse(json_str, content_type="text/json")


def _get_base_json():
  json_str = ""
  with open("../public-did.json", 'r', encoding = 'utf-8') as f:
    json_str = f.read()
    f.close()
  return json.loads(json_str)