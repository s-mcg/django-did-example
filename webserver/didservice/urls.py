from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('.well-known/did.json', views.did_json, name='well-known'),
]