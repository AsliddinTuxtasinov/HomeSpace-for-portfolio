from django.shortcuts import render

# Create your views here.

def index(request, username):
    return render(request, "personal_area/personal_area.html")