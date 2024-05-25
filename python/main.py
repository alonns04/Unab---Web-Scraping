import requests
from bs4 import BeautifulSoup
import openpyxl

workbook = openpyxl.Workbook() # Genera un excel
hoja_activa = workbook.active # Abre el excel

productos_array_meli = [] # Lista con los productos y sus características. precio, nombre, etc.

string_busqueda = input("¿Qué buscamos?")

r_meli = requests.get('https://listado.mercadolibre.com.ar/{}'.format(string_busqueda.replace(' ', '-'), string_busqueda)) # Hace el request y reemplaza los espacios con "-" (No respeta las mayúsculas ni las minúsculas)
contenido_meli = r_meli.content # Ingresa al content del request "r"

soup_meli = BeautifulSoup(contenido_meli, 'html.parser') # Parsea el contenido



productos_meli = soup_meli.find_all('div', class_='ui-search-result__content-wrapper')


for i in productos_meli: # Itera en todo el código html
    producto = i.find("h2")
    precio = i.find("span", class_="andes-money-amount__fraction")
    if producto and precio:
        productos_array_meli.append({"nombre": producto.text.strip(), "precio": precio.text.strip()})



for i in range(len(productos_array_meli)): # Itera y lo va metiendo en el excel
    hoja_activa.cell(row = i + 1, column = 1, value = productos_array_meli[i]["nombre"])
    hoja_activa.cell(row = i + 1, column = 2, value = productos_array_meli[i]["precio"])


ruta_guardado = '../excel/productos.xlsx'
workbook.save(ruta_guardado)