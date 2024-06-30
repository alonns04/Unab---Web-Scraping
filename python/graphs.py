import matplotlib.pyplot as plt
import numpy as np

def graph(product, dolar, dolar_nombre, page):
    products = product.array_products
    data = products[:20]
    list_products_price = [[i['nombre'], i['precio'], i['moneda']] for i in data]

    # Separar nombres y precios
    nombres = [producto[0] for producto in list_products_price]

    def convert_price(producto):
        precio = producto[1]
        moneda = producto[2]
        precio = str(precio)
        precio_str = str(precio)
        if precio[-3] == ".":
            centavos = float(f"0.{precio_str[-2:]}")
            precio = float(precio_str[:-3].replace('.', '')) + centavos
        elif precio[-2] == ".":
            centavos = float(f"0.{precio_str[-1:]}")
            precio = float(precio_str[:-2].replace('.', '')) + centavos
        else:
            precio = float(precio_str.replace('.', ''))
        if moneda == 'ARS':
            return "{:.2f}".format(precio / dolar)
        else:
            return "{:.2f}".format(precio)
        
    precios = [convert_price(producto) for producto in list_products_price]

    # Usar una paleta de colores más grande y seleccionar colores de forma más inteligente
    colors = plt.cm.tab20(np.linspace(0, 1, len(nombres)))

    # Ajustar manualmente las posiciones en el eje x para distribuir uniformemente los puntos
    x_pos = np.arange(len(nombres)) + 1  # Comienza desde 1

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(20, 12))  # Tamaño de la figura

    # Scatter plot para los precios
    for i, (nombre, precio) in enumerate(zip(nombres, precios)):
        ax.scatter(x_pos[i], float(precio), label=nombre, color=colors[i])

    # Etiquetas y título
    ax.set_xlabel('Primeros 20 Productos')
    ax.set_ylabel(f'Precio (USD)')
    ax.set_title(f'Productos de {page} con: {dolar_nombre}')

    plt.subplots_adjust(left=0.15, right=0.65, top=0.9, bottom=0.1)

    # Añadir leyenda
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small') 
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x_pos, rotation='vertical', fontsize=8)

    # Añadir cuadrícula
    ax.grid(True)

    plt.show()

