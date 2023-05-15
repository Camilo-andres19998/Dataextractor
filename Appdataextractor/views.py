import requests
from .models import BikeStation
from django.http import JsonResponse

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
