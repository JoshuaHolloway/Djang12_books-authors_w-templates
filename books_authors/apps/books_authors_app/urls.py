from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^books/add$', views.add),
  url(r'^books/(?P<my_val>\d+)$', views.show),   # e.g., localhost:8000/bears/23
  url(r'^books/assign_author/(?P<book_id>\d+)/(?P<author_id>\d+)$', views.assign_author)   # e.g., localhost:8000/bears/23
]
