from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Reklama, Region, District, SaleRent

import json
from django.core import serializers
from django.core.files.storage import FileSystemStorage

from PIL import Image


# Create your views here.

def index(request, username):
    #user = User.objects.filter( username = username )
    #elonlar = Reklama.objects.filter( author = request.user )
    
    return render(request, "personal_area/personal_area.html") #, { 'elonlar': elonlar, 'user' : user }



def add_reklama(request, username):
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer(District.objects.all(), ensure_ascii=False)
    sale_rents = SaleRent.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        more_info=request.POST['more_info']
        comfort=request.POST['comfort']
        home_type=request.POST['home_type']
        prise = request.POST['prise']
        
        region_id=request.POST['region_id']
        district_id=request.POST['district_id']
        adress = request.POST['adress']
        sale_rent_id=request.POST["sale_rent_id"]
        image=request.FILES.getlist('image')
        phone = request.POST.get('phone', '')

        reklama = Reklama(
            title=title,
            more_info=more_info,
            region_id=region_id,
            district_id=district_id,
            adress=adress,
            sale_rent_id=sale_rent_id,
            prise=prise,
            comfort=comfort,
            img=image,
            phone=phone,
            author = username
        )
        reklama.save()

        return render(request,"add_reklama.html",{
            'regions':regions,
            'districts':districts,
            'sale_rents':sale_rents
        })
    else:
        return HttpResponse(request,"ishlamayapti")





    #return render(request, "personal_area/add_reklama.html")