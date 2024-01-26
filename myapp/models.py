from django.db import models

class Book(models.Model):
  bid = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  publisheddate = models.DateField()