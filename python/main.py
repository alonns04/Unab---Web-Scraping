from amazon import Amazon
from mercado_libre import MercadoLibre
from excels import create_excel
from graphs import graph

def main():
    elemento = input("Ingrese el elemento a buscar: ")
    PRODUCT_AMAZON = Amazon(elemento)
    PRODUCT_MELI = MercadoLibre(elemento)
    create_excel(PRODUCT_AMAZON)
    create_excel(PRODUCT_MELI)
    graph(PRODUCT_AMAZON)
    graph(PRODUCT_MELI)

if __name__ == "__main__":
    main()
    