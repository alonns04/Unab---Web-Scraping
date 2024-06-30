import matplotlib.pyplot as plt
import numpy as np

def graph(product):
    products = product.array_products
    data = products[:5]
    print(data)
    list_products_price = [[i['nombre'], i['precio']] for i in data]
    print(list_products_price)