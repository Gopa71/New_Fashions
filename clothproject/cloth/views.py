from django.shortcuts import render,redirect
from .models import Category,Product
from django.shortcuts import get_object_or_404

# Create your views here.
def home(req):
    return render(req,'home.html')

def mens(req,c_slug=None):
    c_page=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prodcut_list=Product.objects.filter(category=c_page,available=True)
    else:
        prodcut_list=Product.objects.filter(available=True)

        
    return render(req,'mens.html',{'data':prodcut_list,'category':c_page})

def details(req,id):
     data=Product.objects.get(id=id)
     return render(req,'details.html',{'data':data})