from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib



class Amazon():
    def __init__(self, product_name: str):
        self.product_name = product_name
        self.array_products = [] # Lista con los productos y sus características. precio, nombre, etc.
        self.excel_path = '\producto-{}-AMZ.xlsx'.format(self.get_product_name().replace(" ","_").replace("-","_"))
        self.link_product = self.generar_link_amazon()
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0", "Accept-Encoding":"gzip, deflate, br, zstd", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        self.requests = requests.get(self.get_link_product(), headers=self.headers)
        self.html_content = BeautifulSoup(self.requests.content, "html.parser")
        self.all_pages()
        self.divs = self.html_content.find_all("div", class_="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small gsx-ies-anchor sg-col-12-of-16")
        if len(self.divs) == 0:
            self.divs = self.html_content.find_all("div", class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1o8fah2gdzrpk2871rsdu92m5n s-latency-cf-section puis-card-border")
        self.create_filter_list()


    def get_link_product(self):
        return self.link_product
        
    def get_product_name(self):
        return self.product_name
    def generar_link_amazon(self):
        texto_limpio = self.product_name.strip().replace(" ", "+")
        base_url = "https://www.amazon.com/s?k="
        url_completa = f"{base_url}{texto_limpio}&__mk_es_US=ÅMÅŽÕÑ&crid=&sprefix=&ref=nb_sb_noss"
        return url_completa
    
    
    def create_filter_list(self):
        for i in self.divs: # Itera en los divs de la página y extra la información
            producto = i.find("span", class_="a-size-medium a-color-base a-text-normal")
            try: 
                producto = producto.text
            except:
                try:
                    producto = i.find("span", class_="a-size-medium a-color-base a-text-normal").text
                except:
                    try:
                        producto = i.find("span", class_="a-size-base-plus a-color-base a-text-normal").text
                    except:
                        producto = self.product_name
            link = "https://www.amazon.com/-/es" + i.find("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").get("href")

            moneda = "USD"
            price = i.find("span", class_="a-price-whole")
            cents = i.find("span", class_="a-price-fraction")

            if price and price.text:
                price = price.text.split(".")[0].replace(',','')
                if cents:
                    price = float(int(price) + int(cents.text) / 100)
                self.array_products.append({
                    "nombre": producto,
                    "precio": price,
                    "moneda": moneda,
                    "link": link
                })
    
    def all_pages(self):
        next_link = self.html_content.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
        index = 0
        if next_link:
            next_page_url = "https://www.amazon.com/-/es" + next_link.get('href')
            while next_page_url:
                if index < 3:
                    new_request = requests.get(next_page_url, headers=self.headers)
                    new_html_content = new_request.content
                    new_soup_parsed = BeautifulSoup(new_html_content, 'html.parser')
                    self.html_content.append(new_soup_parsed)
                    next_link = self.html_content.find('a', {'class': 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator'})
                    index += 1
                else: 
                    break

    def __str__(self):
        return self.array_products
