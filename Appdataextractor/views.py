import requests
from django.shortcuts import render
from .models import BikeStation
from django.http import JsonResponse
from .utils import obtener_informacion_total, guardar_informacion_json
import json
from .models import Sancionario

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




def obtener_informacion_pagina(request):
    url = 'https://snifa.sma.gob.cl/Sancionatorio/Resultado'
    informacion = obtener_informacion_total(url)
    guardar_informacion_json(informacion, './archivo.json')

    for datos in informacion:
       informacion_modelo = Sancionario()
       informacion_modelo.id = datos['#']
       informacion_modelo.expediente = datos['Expediente']
       informacion_modelo.unidad_fiscalizable = datos['Unidad Fiscalizable']
       informacion_modelo.nombre_razon_social = datos['Nombre razón social']
       informacion_modelo.categoria = datos['Categoría']
       informacion_modelo.region = datos['Región']
       informacion_modelo.estado = datos['Estado']
       informacion_modelo.detalle = datos['Detalle']
       informacion_modelo.save()

    return render(request, 'tabla.html', {'informacion': informacion})