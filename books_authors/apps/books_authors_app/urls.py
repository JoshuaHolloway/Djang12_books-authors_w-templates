from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^josh$', views.show),
  url(r'^books/(?P<my_val>\d+)$', views.show)    # would match localhost:8000/bears/23
]
