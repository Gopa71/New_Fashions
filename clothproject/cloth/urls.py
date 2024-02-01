
from django.urls import path
from . import views
app_name='cloth'
urlpatterns = [
    path('',views.home,name='home'),
    path('mens/',views.mens,name='mens'),
    path('<slug:c_slug>',views.mens,name='products_by_category'),
    path('details/<int:id>',views.details,name='details'),
    
    

]