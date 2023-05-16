import requests
from bs4 import BeautifulSoup
import json

def obtener_informacion_tabla(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    tabla = soup.find('table')


    encabezados = []
    for th in tabla.find_all('th'):
        encabezados.append(th.text.strip())

    filas = []
    for fila in tabla.find_all('tr'):
        datos_fila = []
        for td in fila.find_all('td'):
            datos_fila.append(td.text.strip())
        if datos_fila:
            filas.append(datos_fila)

    informacion = []
    for fila in filas:
        if len(fila) == len(encabezados):
            informacion.append(dict(zip(encabezados, fila)))

    return informacion


def obtener_informacion_total(url):
    informacion_total = []

    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

  
    paginacion = soup.find('ul', class_='pagination')
    paginas = paginacion.find_all('li')
    numero_paginas = len(paginas) - 2

    
    for i in range(1, numero_paginas + 1):
        url_pagina = url + '?pagina=' + str(i)
        informacion_pagina = obtener_informacion_tabla(url_pagina)
        informacion_total.extend(informacion_pagina)

    return informacion_total

def guardar_informacion_json(informacion, archivo):
    with open(archivo, 'w') as f:
        json.dump(informacion, f, indent=4)