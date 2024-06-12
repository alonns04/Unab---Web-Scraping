from amazon import Amazon
from mercado_libre import MercadoLibre

elemento = input("Ingrese el elemento a buscar: ")

producto_amazon = Amazon(elemento)
producto_meli = MercadoLibre(elemento)