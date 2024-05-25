import requests
from bs4 import BeautifulSoup
import openpyxl

workbook = openpyxl.Workbook()

hoja_activa = workbook.active

productos_array_meli = []
precios_array_meli = []

# string_busqueda = input("¿Qué buscamos? ") # Dato a buscar
string_busqueda = "calculadora"

r_meli = requests.get('https://listado.mercadolibre.com.ar/{}'.format(string_busqueda.replace(' ', '-'), string_busqueda)) # Hace el request y reemplaza los espacios con "-"
contenido_meli = r_meli.content # Ingresa al content del request "r"

soup_meli = BeautifulSoup(contenido_meli, 'html.parser') # Parsea el contenido



productos_meli = soup_meli.find_all('div', class_='ui-search-result__content-wrapper')


for i in productos_meli:
    producto = i.find("h2")
    precio = i.find("span", class_="andes-money-amount__fraction")
    if producto and precio:
        productos_array_meli.append({"nombre": producto.text.strip(), "precio": precio.text.strip()})

# Guardar en el excel

for i in range(len(productos_array_meli)):
    hoja_activa.cell(row = i + 1, column = 1, value = productos_array_meli[i]["nombre"])
    hoja_activa.cell(row = i + 1, column = 2, value = productos_array_meli[i]["precio"])


ruta_guardado = '../excel/productos.xlsx'
workbook.save(ruta_guardado)