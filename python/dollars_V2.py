import re
import requests
from bs4 import BeautifulSoup

def dollar():
    # Variables para almacenar los valores
    dolarblue_val = None
    dolarmep_val = None
    dolarcripto_val = None


    website = "https://dolarhoy.com/"
    response = requests.get(website)

    if response.status_code ==200:
        soup = BeautifulSoup(response.text, 'html.parser')
    dolarblue = soup.find_all(href="/cotizaciondolarblue")
    for dolarblue in dolarblue:
        dolarblue_val = dolarblue.find(class_="venta")
      
    if  dolarblue_val:
            print("El precio actual del Blue es: ", dolarblue_val.text.strip())
    
    dolarmep = soup.find_all(href="/cotizaciondolarbolsa")
    for dolarmep in dolarmep:
        dolarmep_val = dolarmep.find(class_="venta")
        
    if dolarmep_val:
            print("El precio actual del dolar MEP es: ", dolarmep_val.text.strip())

     
  
# URL de la API de Binance para obtener el precio de un par específico
    url = 'https://api.binance.com/api/v3/ticker/price'

# Parámetros de la solicitud, en este caso el símbolo del par USDT/ARS
    params = {
        'symbol': 'USDTARS'
}

# Hacer la solicitud GET a la API de Binance
    response = requests.get(url, params=params)

    if response.status_code == 200:
        dolarcripto_val = response.json()
        price = dolarcripto_val ['price']
        print(f"El precio actual del dolar cripto es: {price}")
    else:
        print(f"Error en la solicitud: {response.status_code}")

    return {
        'Dólar Blue': dolarblue_val,
        'Dólar MEP': dolarmep_val,
        'Dólar Cripto': dolarcripto_val
    }


