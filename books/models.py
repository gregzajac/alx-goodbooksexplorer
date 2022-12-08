from django.db import models

# Create your models here.


class Book(models.Model):

    bookID = models.IntegerField()
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=10)
    isbn13 = models.IntegerField()
    language_code = models.CharField(max_length=6)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_review_counts = models.IntegerField()
    publication_date = models.DateTimeField()
    publisher = models.CharField(max_length=255)