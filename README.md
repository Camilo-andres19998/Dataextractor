# Dataextractor

Este proyecto consiste en una aplicación Django que utiliza dos fuentes de datos diferentes para obtener información relevante.

La primera fuente es una API pública llamada https://api.citybik.es/v2/networks/bikerio. Se ha desarrollado una función que utiliza las librerías requests, urllib3 o aiohttp para obtener los datos de la API. La información obtenida se guarda en un modelo específico creado para este propósito.

La segunda fuente de datos es una página web con una tabla de información ubicada en https://snifa.sma.gob.cl/Sancionatorio/Resultado. 
Se ha creado un script utilizando las librerías BeautifulSoup o Selenium para extraer 
la información de la tabla. El script recorre todas las páginas y crea un archivo .json con la información obtenida. Además, se genera un modelo para guardar estos datos.

## Requisitos

- Python 3.x
- PostgreSQL (versión X.X)
- Paquetes adicionales:
  - requests
  - beautifulsoup
  - psycopg2

## Instalación

1. Clona el repositorio o descarga el código fuente.

2. Crea un entorno virtual: `python -m venv env`
3. Activa el entorno virtual:
   - En Windows: `.\env\Scripts\activate`
   - En macOS/Linux: `source env/bin/activate`
   
4. Instala los paquetes adicionales:
   - Si utilizas pip: `pip install requests beautifulsoup psycopg2`
   - Si utilizas el archivo `requirements.txt`: `pip install -r requirements.txt`
   - El paquete requests es una librería de Python que permite realizar peticiones HTTP de manera sencilla. Proporciona una interfaz amigable para enviar solicitudes y recibir respuestas HTTP, lo que lo convierte en una herramienta muy útil para interactuar con APIs, enviar formularios web, descargar archivos y más.
   
   > El archivo `requirements.txt` contiene una lista de todos los paquetes y sus versiones requeridos por el proyecto. Al ejecutar este comando, se instalarán automáticamente todas las dependencias necesarias.
   
5. Instala PostgreSQL y configura la base de datos en el archivo `settings.py`:
   - DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           
           'NAME': 'nombre_basedatos',
           
           'USER': 'nombre_usuario',
           
           'PASSWORD': 'contraseña',
           
           'HOST': 'localhost',
           
           'PORT': '5432',
       }
   }
   
   
6. Crea las migraciones: `python manage.py makemigrations`
7. Aplica las migraciones: `python manage.py migrate`

## Uso

1. Inicia el servidor de desarrollo: `python manage.py runserver`
2. Abre tu navegador y accede a: `http://localhost:8000`

## Estructura del Proyecto

Breve descripción de la estructura de archivos y directorios del proyecto.

- `manage.py`: Punto de entrada de la aplicación Django.
- `requirements.txt`: Archivo que lista todas las dependencias del proyecto.
- `config/`: Directorio que contiene la configuración del proyecto.
- `app/`: Directorio que contiene la lógica y los modelos de la aplicación.


## Licencia

Indica la licencia bajo la cual se distribuye el proyecto.



