from django.db import models
from cloth.models import Product
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    user_id=models.IntegerField()


class Order(models.Model):

    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)