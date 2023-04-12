from django.contrib.gis.db import models

class Composter(models.Model):
    orgName = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    composter_location = models.PointField(srid=4326)

    def __str__(self):
        return self.orgName
    
class Greener(models.Model):
    firstName = models.CharField(max_length=12)
    lastName = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    greener_location = models.PointField()
    wallet = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"