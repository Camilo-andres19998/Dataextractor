import requests
from django.shortcuts import render
from .models import BikeStation
from django.http import JsonResponse
from .utils import obtener_informacion_total, guardar_informacion_json
import json
from .models import Sancionario_info
import os

def obtener_informacion_api():
    url = 'https://api.citybik.es/v2/networks/bikerio'
    response = requests.get(url)
    data = response.json()
    return data.get('network', {}).get('stations', [])


def guardar_informacion_en_modelo():
    informacion_api = obtener_informacion_api()
    
    if informacion_api is not None:
        for item in informacion_api:
            existente = BikeStation.objects.filter(name=item.get('name')).exists()
            if not existente:
                instancia = BikeStation.objects.create(
                    name=item.get('name', ''),
                    latitude=item.get('latitude'),
                    longitude=item.get('longitude'),
                    free_bikes=item.get('free_bikes'),
                    empty_slots=item.get('empty_slots')
                )


def obtener_informacion_bikerio(request):
    bike_stations = BikeStation.objects.all()
    data = {
        'bike_stations': list(bike_stations.values()),
    }
    return JsonResponse(data)


def ver_informacion(request):
    guardar_informacion_en_modelo()
    bike_stations = BikeStation.objects.order_by('-id')
    data = {
        'bike_stations': bike_stations
    }
    return render(request, 'bikerio.html', data)


def obtener_informacion(request):
    informacion = Sancionario_info.objects.all()
    return render(request, 'sancionario.html', {'informacion': informacion})


def obtener_informacion_pagina(request):
    url = 'https://snifa.sma.gob.cl/Sancionatorio/Resultado'
    
    try:
        informacion = obtener_informacion_total(url)

        # Reemplazar las claves con tildes por versiones sin tildes en los elementos del diccionario
        for datos in informacion:
            if 'Nombre razón social' in datos:
                datos['Nombre razon social'] = datos.pop('Nombre razón social')
            if 'Categoría' in datos:
                datos['Categoria'] = datos.pop('Categoría')
            if 'Región' in datos:
                datos['Region'] = datos.pop('Región')

        # Ruta de la carpeta donde se almacenará el archivo JSON
        carpeta = 'json'

        # Crear la carpeta si no existe
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        # Ruta completa del archivo JSON
        ruta_json = os.path.join(carpeta, 'archivo.json')

        # Guardar el archivo JSON con la codificación adecuada
        with open(ruta_json, 'w', encoding='utf-8') as file:
            json.dump(informacion, file, ensure_ascii=False)

        for datos in informacion:
            informacion_modelo = Sancionario_info()
            
            informacion_modelo.id = datos['#']
            informacion_modelo.expediente = datos['Expediente']
            informacion_modelo.unidad_fiscalizable = datos['Unidad Fiscalizable']
            informacion_modelo.nombre_razon_social = datos.get('Nombre razon social', '')
            informacion_modelo.categoria = datos.get('Categoria', '')
            informacion_modelo.region = datos.get('Region', '')
            informacion_modelo.estado = datos['Estado']
            informacion_modelo.detalle = datos['Detalle']
            if 'Ver detalles' in datos['Detalle']:
                informacion_modelo.url_detalle = 'https://snifa.sma.gob.cl/Sancionatorio/Ficha/3314'
            informacion_modelo.save()
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud HTTP: {e}')
    except json.JSONDecodeError as e:
        print(f'Error decodificando JSON: {e}')
    
    return obtener_informacion(request)