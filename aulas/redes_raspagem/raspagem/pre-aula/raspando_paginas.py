import requests
from parsel import Selector

BASE_URL = "https://books.toscrape.com/catalogue/"  # url paginação
next_page_url = "page-1.html"  # para comçar na pag 1

while next_page_url:
    response = requests.get(BASE_URL + next_page_url)
    selector = Selector(response.text)
    for product in selector.css(".product_pod"):
        title = product.css("h3 a::attr(title)").get()
        price = product.css("p.price_color::text").get()  # pegando o texto
        print(title, price)

    next_page_url = selector.css(".next a::attr(href)").get()  # proxima pág
    print(next_page_url)
