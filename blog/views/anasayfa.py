from django.shortcuts import render
from django.http import HttpResponse

def anasayfa(request):
    return render(request,"pages/anasayfa.html", context = {})