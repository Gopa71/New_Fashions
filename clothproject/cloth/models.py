from django.db import models
from django.urls import reverse

# Create your models here.

class Gender(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    def __str__(self):
        
        return '{}'.format(self.name)
    
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    desc=models.TextField(blank=True)
    banner=models.ImageField(upload_to='banner',blank=True)
    
    class Meta:
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('cloth:products_by_category',args=[self.slug])
    
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    brand=models.CharField(max_length=250,unique=True)
    rating=models.IntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    photo=models.ImageField(upload_to='pic')
    stock=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        
        return '{}'.format(self.name)
    
