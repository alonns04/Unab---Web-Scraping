import requests
from bs4 import BeautifulSoup

string_busqueda = input("¿Qué buscamos? ") # Dato a buscar
r = requests.get('https://listado.mercadolibre.com.ar/{}'.format(string_busqueda.replace(' ', '-'), string_busqueda)) # Hace el request y reemplaza los espacios con "-"
contenido = r.content # Ingresa al content del request "r"

soup = BeautifulSoup(contenido, 'html.parser') # Parsea el contenido

products_array = []

divs = []