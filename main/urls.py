from django.urls import path
from . import views


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('price/', views.price, name='price'),
    path('service/', views.service, name='service'),
]