from django.contrib import admin
from .models import *


@admin.register(Coffy)
class CoffyAdmin(admin.ModelAdmin):
    list_display=['id','title','photo']     
    prepopulated_fields={'slug':('title',)}    
     

@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display=['id','photo']     
    
