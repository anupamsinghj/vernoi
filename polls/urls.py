from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('a', views.abc),
    path('b', views.bcd),
]
