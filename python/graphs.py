import matplotlib.pyplot as plt
import numpy as np

def graph(product):
    products = product.array_products
    data = products[:20]
    print(data)
    list_products_price = [[i['nombre'], i['precio'], i['moneda']] for i in data]

    # Separar nombres y precios
    nombres = [producto[0] for producto in list_products_price]

    def convert_price(producto, dolar = 1400):
        precio = producto[1]
        moneda = producto[2]
        precio = str(precio)
        precio_str = str(precio)
        if precio[-3] == ".":
            centavos = float(f"0.{precio_str[-2:]}")
            precio = float(precio_str[:-3].replace('.','')) + centavos
        elif precio[-2] == "." :
            centavos = float(f"0.{precio_str[-1:]}")
            precio = float(precio_str[:-2].replace('.','')) + centavos
        else:
            precio = float(precio_str.replace('.',''))
        if moneda == 'USD':
            return "{:.2f}".format(precio * dolar)
        else:
            return "{:.2f}".format(precio)
        
    if data[0]["moneda"] == "USD":
        precios = [convert_price(producto) for producto in list_products_price]
    else:
        precios = [convert_price(producto) for producto in list_products_price]

    print(list_products_price)

    print(precios)
    print(nombres)

    # Usar una paleta de colores más grande y seleccionar colores de forma más inteligente
    colors = plt.cm.tab10(np.linspace(0, 1, len(nombres)))

    # Ajustar manualmente las posiciones en el eje x para distribuir uniformemente los puntos
    x_pos = np.arange(len(nombres))

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(20, 12))  # Tamaño de la figura

    # Scatter plot para los precios
    for i, (nombre, precio) in enumerate(zip(nombres, precios)):
        ax.scatter(x_pos[i], precio, label=nombre, color=colors[i])

    # Etiquetas y título
    ax.set_xlabel('Productos')
    ax.set_ylabel('Precio (ARS)')
    ax.set_title('Precios de Productos')
    ax.set_xticks([])  # Eliminar los ticks del eje x

    plt.subplots_adjust(left=0.15, right=0.5, top=0.9, bottom=0.1)

    # Añadir leyenda
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')

    plt.show()

# Ejemplo de uso
# Suponiendo que tienes la función product.array_products para obtener los datos
# y la función convert_price definida como en tu código original
# graph(product)
