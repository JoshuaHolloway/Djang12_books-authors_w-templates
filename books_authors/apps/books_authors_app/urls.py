from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^books/add$', views.add),
  url(r'^books/(?P<my_val>\d+)$', views.show)   # e.g., localhost:8000/bears/23
  # url(r'^books/add$', views.add)    # would match localhost:8000/bears/23
]
