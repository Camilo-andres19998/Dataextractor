from django.urls import path
from . import views

app_name = 'Appdataextractor'

urlpatterns = [
    path('guardar-informacion/', views.guardar_informacion_en_modelo, name='guardar_informacion'),
    path('obtener-informacion/', views.obtener_informacion_api, name='obtener_informacion'),
]
