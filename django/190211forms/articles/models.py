from django.db import models

# Create your models here.
class Food(models.Model) :
    kind = models.CharField(max_length=30)
    name = models.TextField()
    cal = models.IntegerField()
    materials = models.TextField()
    