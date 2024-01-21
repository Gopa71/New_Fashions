from django.contrib import admin
from .models import  Category,Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}


admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','brand','stock','available','created','updated','slug','photo','rating']
    list_editable=['price','rating','stock','available']
    list_per_page=20
    prepopulated_fields={'slug':('name',)}

admin.site.register(Product,ProductAdmin)