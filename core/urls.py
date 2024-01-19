from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='admin'),
    path('home', index, name='home'),
]