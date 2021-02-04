from django.db import models
from django.contrib.auth.models import User


class Region(models.Model): # viloyatlarni kiritish uchun
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class District(models.Model): # tumanlarni kiritish uchun
    name = models.CharField(max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class SaleRent(models.Model): # sotish yoki ijaraga berish uchun
    name = models.CharField(max_length=10, default="For_sale")

    def __str__(self):
        return self.name






class Reklama(models.Model): # reklama kiritish uchun
    title = models.CharField(max_length=50) # sarlavha (reklama1)
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # buni togirlash kerak, reklama beruvchi username si 
    prise = models.FloatField() # narxni kiritish uchun
    img = models.ImageField(upload_to='reklama_images') # reklama rasmini kiritish uchun
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True,blank=True) # viloyatlrni kiritish uchun
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True,blank=True) # tumanlarni kiritish uchun
    sale_rent = models.ForeignKey(SaleRent, on_delete=models.CASCADE, default="For_sale") # buni togirlash kerak, sotish yoki ijaraga berish
    adress = models.CharField(max_length=80, default = '') # adresni kritish uchun
    more_info = models.TextField(null=True,blank=True) # reklama haqida koproq malumotlar
    comfort = models.TextField(default = 'medium') # quaylikarini kiritish (wi fi, holadelnik, ...)
    home_type = models.CharField(max_length=50,default = 'house') # sotiladigan uy turi (kvartira, hovli, kop qavatli uy, magazin, ..)
    phone = models.CharField(max_length=50, null=True) # sotuvchining telefon nomeri
    author = models.CharField(max_length=50) # reklama beruvchi
    
    def __str__(self):
        return self.title