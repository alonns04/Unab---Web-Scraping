import matplotlib.pyplot as plt
import numpy as np

def graph(product):
    products = product.array_products
    data = products[:5]
    print(data)
    productos = [
    {'nombre': 'Calculadora Cientifica Casio Fx-991lacw Classwiz', 'precio': '78.139', 'moneda': 'ARS', 'link': 'https://www.mercadolibre.com.ar/calculadora-cientifica-casio-fx-991lacw-classwiz/p/MLA23027132#searchVariation=MLA23027132&position=1&search_layout=grid&type=product&tracking_id=218d78d9-9c5a-4a19-b21b-96abce523b6f'}, 
    {'nombre': 'Calculadora Cientifica Casio Fx-82ms 240 Funciones Estuche Color Negro', 'precio': '28.459', 'moneda': 'ARS', 'link': 'https://www.mercadolibre.com.ar/calculadora-cientifica-casio-fx-82ms-240-funciones-estuche-color-negro/p/MLA24112614#searchVariation=MLA24112614&position=2&search_layout=grid&type=product&tracking_id=218d78d9-9c5a-4a19-b21b-96abce523b6f'}, 
    {'nombre': 'Calculadora Cientifica Fx-82ms Casio marrón oscuro', 'precio': '27.036', 'moneda': 'ARS', 'link': 'https://www.mercadolibre.com.ar/calculadora-cientifica-fx-82ms-casio-marron-oscuro/p/MLA23958967#searchVariation=MLA23958967&position=6&search_layout=grid&type=product&tracking_id=218d78d9-9c5a-4a19-b21b-96abce523b6f'}, 
    {'nombre': 'Calculadora Cientifica Casio Fx 570la Cw Classwiz Negra', 'precio': '72.999', 'moneda': 'ARS', 'link': 'https://www.mercadolibre.com.ar/calculadora-cientifica-casio-fx-570la-cw-classwiz-negra/p/MLA22724798#searchVariation=MLA22724798&position=4&search_layout=grid&type=product&tracking_id=218d78d9-9c5a-4a19-b21b-96abce523b6f'}, 
    {'nombre': 'Calculadora Casio Científica Fx-82la-cw Fx-82lac 2da Edicion Color Negro', 'precio': '35.782', 'moneda': 'ARS', 'link': 'https://www.mercadolibre.com.ar/calculadora-casio-cientifica-fx-82la-cw-fx-82lac-2da-edicion-color-negro/p/MLA25707828#searchVariation=MLA25707828&position=3&search_layout=grid&type=product&tracking_id=218d78d9-9c5a-4a19-b21b-96abce523b6f'}
]

lista_productos = [[producto['nombre'], producto['precio']] for producto in productos]

print(lista_productos)
