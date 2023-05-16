import requests
from django.shortcuts import render
from .models import BikeStation
from django.http import JsonResponse
from .utils import obtener_informacion_total,guardar_informacion_json

def obtener_informacion_api():
    url = 'https://api.citybik.es/v2/networks/bikerio'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('network', {}).get('stations', [])
    
    return None


def guardar_informacion_en_modelo():
    informacion_api = obtener_informacion_api()
    
    if informacion_api is not None:
        for item in informacion_api:
            instancia = BikeStation(
                name=item['name'],
                latitude=item['latitude'],
                longitude=item['longitude'],
                free_bikes=item['free_bikes'],
                empty_slots=item['empty_slots']
            )
            instancia.save()

def obtener_informacion(request):
    guardar_informacion_en_modelo()
    bike_stations = BikeStation.objects.all()
    data = {
        'bike_stations': list(bike_stations.values()),
    }
    return JsonResponse(data)


def ver_informacion(request):
    bike_stations = BikeStation.objects.order_by('id')
    
    data = {
        'bike_stations': bike_stations
    }
    return render(request, 'bikerio.html', data)


def paginas_view(request):
   
   url = 'https://snifa.sma.gob.cl/Sancionatorio/Resultado'

   informacion_total = obtener_informacion_total(url)

   archivo_json = 'informacion_paginas.json'
   guardar_informacion_json(informacion_total, archivo_json)



   context = {
        'informacion': informacion_total,
        'archivo_json': archivo_json,
    }
   
   return render(request,'tabla.html', context)