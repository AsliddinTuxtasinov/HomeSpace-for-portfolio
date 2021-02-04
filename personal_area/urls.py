from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index, name = "personal"),
    path('add_reklama/', views.add_reklama, name = "add_reklama"),


]
