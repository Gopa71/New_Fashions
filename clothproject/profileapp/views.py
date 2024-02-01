from django.shortcuts import render
from .models import Profile
# Create your views here.
def profile(req):
    
    return render(req,'Myprofile.html')

def address(req):
    value=Profile.objects.all()
    if req.method=='POST':
        name=req.POST['name']
        phone=req.POST['phone']
        picode=req.POST['picode']
        address=req.POST['address']
        district=req.POST['district']
        landmark=req.POST['landmark']
        tk=Profile(name=name,phone=phone,picode=picode,address=address,district=district,landmark=landmark)
        tk.save()
    return render(req,'cart.html',{'value':value})