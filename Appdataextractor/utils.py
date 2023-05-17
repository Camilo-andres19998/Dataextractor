import requests
from bs4 import BeautifulSoup
import json

# Función que recibe una URL y devuelve la información contenida en una tabla como una lista de diccionarios
def obtener_informacion_tabla(url):
    response = requests.get(url)  # Hacemos una petición GET a la URL
    soup = BeautifulSoup(response.text, 'html.parser')

    tabla = soup.find('table')
    if tabla is None:
        return None
    
 # Obtener los encabezados de la tabla
    encabezados = [th.text.strip() for th in tabla.find_all('th')]
# Obtener las filas de la tabla
    filas = []
    for fila in tabla.find_all('tr'):
         # Obtener los datos de cada celda de la fila
        datos_fila = [td.text.strip() for td in fila.find_all('td')]
        if datos_fila:
            filas.append(datos_fila)
            
# Crear una lista de diccionarios con la información de la tabla
    informacion = []
    for fila in filas:
        if len(fila) == len(encabezados):
            informacion.append(dict(zip(encabezados, fila)))

    return informacion

# Función que recibe una URL y devuelve la información contenida en todas las páginas de la tabla como una lista de diccionarios
def obtener_informacion_total(url):
    informacion_total = []

    response = requests.get(url) # Hacemos una petición GET a la URL
    soup = BeautifulSoup(response.text, 'html.parser') # Crear una instancia de BeautifulSoup

    paginacion = soup.find('ul', class_='pagination')
    if paginacion is None:
        numero_paginas = 1
    else:
        paginas = paginacion.find_all('li')
        numero_paginas = len(paginas) - 2

    for i in range(1, numero_paginas + 1):
        url_pagina = url + '?pagina=' + str(i)
         # Obtener la información de la tabla en la página actual
        informacion_pagina = obtener_informacion_tabla(url_pagina)
        if informacion_pagina is not None:
            # Agregar la información de la página actual a la lista total
            informacion_total.extend(informacion_pagina)

    return informacion_total

def guardar_informacion_json(informacion, archivo):
    with open(archivo, 'w', encoding='utf-8') as file:
        json.dump(informacion, file, indent=4, ensure_ascii=False)
