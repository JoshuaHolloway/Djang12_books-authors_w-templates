from django.db import models
# ======================================================================================================================
# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Book: ({self.title})"
# ======================================================================================================================
class Author(models.Model):
  name = models.CharField(max_length=255)
  notes = models.TextField()
  books = models.ManyToManyField(Book, related_name="authors")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __repr__(self):
    return f"Author: ({self.name})"
# ======================================================================================================================