from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'myweb'

urlpatterns = [
    path('b', views.bcd),
    path('ba', views.ba),
    path('m18', views.m18,name='map')
]
