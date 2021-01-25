from django.shortcuts import render

# Create your views here.
def home(request):
    return render( request, 'index.html')

def nav_bar(request):
    return render( request, 'navbar-footer.html')

def contact(request):
    return render( request, 'contact.html')

def about(request):
    return render( request, 'about.html')

def blog(request):
    return render( request, 'blog.html')

def properties(request):
    return render( request, 'properties.html')

def property_details(request):
    return render( request, 'property-details.html')