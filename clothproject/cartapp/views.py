from django.shortcuts import render,redirect
from cloth.models import Product
from .models import Cart,Order
from profileapp.models import Profile
# Create your views here.
def cart(req,id):
     product=Product.objects.get(id=id)
     user_id=None
     try:
          user_id = req.session["user"]
     except:
            return redirect('reg:login')
     try:
       user_id = req.session["user"]
       cartitem=Cart.objects.get(product=product,user_id=user_id)
       
       if cartitem.quantity<cartitem.product.stock:
           cartitem.quantity += 1
           cartitem.save()
           

     except:
        
        user_id = req.session["user"]
        cartitem=Cart(product=product,user_id=user_id,quantity=1)
        cartitem.save()
    
     cartitem=Cart.objects.get(product=product,user_id=user_id)
   
        
     return redirect(('cart:display'))
     
def display(req):
    value=Profile.objects.all()
    user_id = req.session["user"]
    print('user_is',user_id)
    data=Cart.objects.all().filter(user_id=user_id)
    total_amount=sum(i.product.price * i.quantity  for i in data)
    print(data)
    return render(req,'cart.html', {'data': data,'total_amount':total_amount,'value':value})   


def delete(req,id):
     user_id = req.session["user"]
     product=Product.objects.get(id=id)
     data=Cart.objects.get(product=product,user_id=user_id)
     data.delete()
     
     
     return redirect('cart:display')

def remove(req,id):

    user_id = req.session["user"]
    product=Product.objects.get(id=id)
    cartitem=Cart.objects.get(product=product,user_id=user_id)
    if cartitem.quantity>1:
           cartitem.quantity -= 1
           cartitem.save()
    else:
      cartitem.delete()
          
    return redirect(('cart:display'))


def buy(req):

    cart_items = Cart.objects.all()

    for cart_item in cart_items:
        # product = cart_item.product
        # quantity_to_purchase = cart_item.quantity

        if cart_item.product.stock >= cart_item.quantity:
            cart_item.product.stock -= 1
            cart_item.product.save()
            order=Order(quantity=cart_item.quantity,price=cart_item.product.price,product_id=cart_item.product.id)
            order.save()

            cart_item.delete()
        else:
            
            return redirect('cart:display')
    return redirect('/')


    