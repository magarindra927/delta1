from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


    
class Coffy(models.Model):    
    title=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    summary=RichTextField()
    content=RichTextField()    
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)

class Coffee(models.Model):    
    
    content=RichTextField()    
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)



    


