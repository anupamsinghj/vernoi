from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def abc(request):
    return render(request, "polls/abc.html")
def bcd(request):
    return render(request, "polls/bcd.html")
