import requests
from bs4 import BeautifulSoup
import openpyxl
import re

workbook = openpyxl.Workbook() # Genera un excel
hoja_activa = workbook.active # Abre el excel

def meli_string1(string): # Reemplaza los espacios por _
    string = string.strip().lower()
    return re.sub(r'\s+', '_', string)

def meli_string2(string): # Reemplaza los espacios por "20%"
    return string.replace(" ", "%20")

productos_array_meli = [] # Lista con los productos y sus características. precio, nombre, etc.

string_busqueda = input("¿Qué buscamos?: ")

r_meli = requests.get('https://listado.mercadolibre.com.ar/{}#D[A:{}]'.format(meli_string1(string_busqueda), meli_string2(string_busqueda))) # Hace el request y reemplaza los espacios con "-" (No respeta las mayúsculas ni las minúsculas)

contenido_meli = r_meli.content # Ingresa al content del request "r"

soup_meli = BeautifulSoup(contenido_meli, 'html.parser') # Parsea el contenido



productos_meli = soup_meli.find_all('div', class_='ui-search-result__content-wrapper')


for i in productos_meli: # Itera en todo el código html
    producto = i.find("h2")
    moneda = i.find("span", class_="andes-money-amount__currency-symbol")
    precio = i.find("span", class_="andes-money-amount__fraction")
    link = i.find("a")["href"]
    if producto and precio:
        productos_array_meli.append({"nombre": producto.text.strip(), "precio": precio.text.strip(), "moneda": moneda.text.strip(), "link": link})


for i in range(len(productos_array_meli)): # Itera y lo va metiendo en el excel
    hoja_activa.cell(row = i + 1, column = 1, value = productos_array_meli[i]["nombre"])
    hoja_activa.cell(row = i + 1, column = 2, value =  productos_array_meli[i]["moneda"])
    hoja_activa.cell(row = i + 1, column = 3, value =  productos_array_meli[i]["precio"])
    hoja_activa.cell(row = i + 1, column = 4, value =  productos_array_meli[i]["link"])

ruta_guardado = '../excel/producto_{}.xlsx'.format(string_busqueda)
workbook.save(ruta_guardado)
