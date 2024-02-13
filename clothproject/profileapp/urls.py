
from django.urls import path
from . import views
app_name='profile'
urlpatterns = [
path('profile/',views.profile,name='profile'),  
path('address/',views.address,name='address') ,
path('delete/<int:id>',views.delete,name='delete')

]