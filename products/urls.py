from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.index,name='home'),
    path('about/',views.about,name='about_page'),
    path('contact/',views.contact,name='contact_page'),
    path('collections/<str:category>/',views.product_list,name='shop_page'),
    path('product_details/<int:product_id>/',views.product_details,name='product_details'),



   

]