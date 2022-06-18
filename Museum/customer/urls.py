from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('shop',views.shop,name='shop'),
    path('bookticket',views.bookticket,name='bookticket'),
    path('event',views.event,name='event')
]