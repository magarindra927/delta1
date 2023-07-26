from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def coffee(request):
    data={
        'coffeeData':Coffee.objects.all(),
    }
    return render(request, 'coffee.html', data)

def coffy_details(request, slug):
    data={
        'coffyData':Coffy.objects.get(slug=slug)
    }   
    return render(request, 'coffy-details.html', data)


