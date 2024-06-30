import re
import requests
from bs4 import BeautifulSoup

website = "https://dolarhoy.com/"
response = requests.get(website)

if response.status_code ==200:
    soup = BeautifulSoup(response.text, 'html.parser')
    dolarblue = soup.find_all(href="/cotizaciondolarblue")
    for dolarblue in dolarblue:
        titulo = dolarblue.find(class_="venta")
        if titulo:
            print("el valor del dolar blue es: ", titulo.text.strip())

else:
    print("Error al cargar la web, codigo: ", response.status_code)


# URL de la API de Binance para obtener el precio de un par específico
url = 'https://api.binance.com/api/v3/ticker/price'

# Parámetros de la solicitud, en este caso el símbolo del par USDT/ARS
params = {
    'symbol': 'USDTARS'
}

# Hacer la solicitud GET a la API de Binance
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    price = data['price']
    print(f"El precio actual de USDT/ARS es: {price}")
else:
    print(f"Error en la solicitud: {response.status_code}")
