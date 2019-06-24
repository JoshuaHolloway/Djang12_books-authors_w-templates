from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.books),

  url(r'^books/add_book$', views.add_book),
  url(r'^books/(?P<book_id>\d+)$', views.show_book),   # e.g., localhost:8000/books/23
  url(r'^books/assign_author/(?P<book_id>\d+)$', views.assign_author),
  url(r'^books/assign_author/(?P<book_id>\d+)/(?P<author_id>\d+)$', views.assign_author_redirected),



  url(r'^authors$', views.authors),

  url(r'^authors/add_author$', views.add_author),
  url(r'^authors/(?P<author_id>\d+)$', views.show_author),   # e.g., localhost:8000/authors/23
  url(r'^authors/assign_book/(?P<author_id>\d+)', views.assign_book),
  url(r'^author/assign_book/(?P<author_id>\d+)/(?P<book_id>\d+)', views.assign_book_redirected)
]