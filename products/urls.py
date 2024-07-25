from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.index,name='home'),
    path('about/',views.about,name='about_page'),
    path('contact/',views.contact,name='contact_page'),


   

]