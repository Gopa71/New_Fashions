from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    picode=models.IntegerField()
    address=models.TextField()
    district=models.TextField()
    landmark=models.TextField()
    