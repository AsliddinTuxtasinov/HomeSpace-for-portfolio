from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('contact/', views.contact, name = "contact"),
    path('about/', views.about, name = "about"),
    path('blog/', views.blog, name = "blog"),
    path('properties/', views.properties, name = "properties"),
    path('property-details/', views.property_details, name = "property-details"),
    #path('add_reklama/', views.add_reklama, name = 'add_reklama'),



    path('navfoot/', views.nav_bar),
]
