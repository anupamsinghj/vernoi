from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bcd(request):
    return render(request, "myweb/bcd.html")
def ba(request):
    return render(request, "myweb/1.html")
def m18(request):
        return render(request, "myweb/map18.html")
