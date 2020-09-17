from django.db import models
# Create your models here.
from uuid import uuid4


class MovieModel(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)
    vote_average = models.FloatField()
    vote_count = models.FloatField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=300, null=True)
    overview = models.TextField()
    budget = models.BigIntegerField()
    revenue = models.BigIntegerField()
    genres = models.CharField(max_length=400)
    runtime = models.IntegerField(null=True)
    id = models.CharField(unique=True, primary_key=True, max_length=100)

    class Meta:
        ordering = ['-release_date']
