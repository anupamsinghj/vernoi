from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bcd(request):
    return render(request, "myweb/bcd.html")
