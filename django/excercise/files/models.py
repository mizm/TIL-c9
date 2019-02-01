from django.db import models

# Create your models here.
class Movie(models.Model) :
    title_kr = models.TextField()
    title_en = models.TextField()
    spectators = models.IntegerField()
    summary = models.TextField()
    info_url = models.TextField()
    score = models.FloatField()
    genre = models.TextField()
    poster = models.ImageField(blank=True)
    picture1 = models.ImageField(blank=True)
    picture2 = models.ImageField(blank=True)
    picture3 = models.ImageField(blank=True)