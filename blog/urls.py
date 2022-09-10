from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.detalle_post, name='detalle_post'),
]