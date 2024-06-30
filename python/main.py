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

    dollars_list = [["Dólar Cripto", 1493], ["Dólar Mep", 1378], ["Dólar Blue", 1428]]

    for dolar_nombre, dolar_valor in dollars_list:
        graph(PRODUCT_AMAZON, dolar_valor, dolar_nombre, "Amazon")
        graph(PRODUCT_MELI, dolar_valor, dolar_nombre, "Mercado Libre")

if __name__ == "__main__":
    main()
    