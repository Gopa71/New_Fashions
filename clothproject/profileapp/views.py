from django.shortcuts import render,redirect
from .models import Profile
# Create your views here.
def profile(req):
    value=Profile.objects.all()
    return render(req,'Myprofile.html',{'value':value})

def address(req):
    value=None
    if req.method=='POST':
        name=req.POST['name']
        phone=req.POST['phone']
        picode=req.POST['picode']
        address=req.POST['address']
        district=req.POST['district']
        landmark=req.POST['landmark']
        tk=Profile(name=name,phone=phone,picode=picode,address=address,district=district,landmark=landmark)
        tk.save()
        return redirect('profile:profile')
    return render(req,'address.html')    
    
def delete(req,id):
     data=Profile.objects.get(id=id)
     data.delete()
     return redirect('profile:profile')