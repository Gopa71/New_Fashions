from .models import Category,Gender


def men(req):
    men=Gender.objects.get(name='men') 
    men=Category.objects.all().filter(gender=men)
    return dict(men=men)
def women(req):
    women=Gender.objects.get(name='women')
    women=Category.objects.all().filter(gender=women)
    return dict(women=women) 