from django.contrib.gis.db import models

class Composter(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    point = models.PointField()
