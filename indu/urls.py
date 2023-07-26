from django.urls import path, include
from .import views

urlpatterns = [
   path('',views.index, name='index'),
   path('about',views.about, name='about'),
   path('contact', views.contact, name='contact'),
   path('coffee', views.coffee, name='coffee'),
   path('coffy-details/<slug>', views.coffy_details, name='coffy_details'),
]
   
