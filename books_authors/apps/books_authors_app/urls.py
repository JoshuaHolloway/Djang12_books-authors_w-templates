from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.books),
  url(r'^authors$', views.authors),
  url(r'^books/add$', views.add),
  url(r'^books/(?P<my_val>\d+)$', views.show),   # e.g., localhost:8000/books/23
  url(r'^authors/(?P<my_val>\d+)$', views.show_authors),   # e.g., localhost:8000/authors/23
  url(r'^books/assign_author/(?P<book_id>\d+)/(?P<author_id>\d+)$', views.assign_author),
  url(r'^authors/assign_book/(?P<author_id>\d+)/(?P<book_id>\d+)', views.assign_book)
]