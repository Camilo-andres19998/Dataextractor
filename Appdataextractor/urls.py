from django.urls import path
from . import views

app_name = 'Appdataextractor'

urlpatterns = [
  path('', views.obtener_informacion, name='obtener_informacion'),
]
