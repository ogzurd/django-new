from django.shortcuts import render,redirect
from blog.forms import IletisimForm
from blog.models import IletisimModel



def email_gonderildi(request):
     return render(request, "pages/email-gonderildi.html")

   
    