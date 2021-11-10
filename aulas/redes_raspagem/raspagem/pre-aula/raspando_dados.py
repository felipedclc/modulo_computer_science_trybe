import requests
from parsel import Selector  # utilizado para selecionar o elemento

# navegando pela página com o parsel

URL_BASE = "https://books.toscrape.com/"
response = requests.get(URL_BASE)
# print(response.status_code)
selector = Selector(response.text)  # a página fica selecionável
# print(selector)
# print(selector.css("img.thumbnail").get())  # get() - pega apenas o 1
# [print(thumbnail) for thumbnail in selector.css("img.thumbnail").getall()]

# print(selector.css("div.image_container a").get())
# print(selector.css("div.image_container a::attr(href)").get())
# thumb_url = selector.css("div.image_container a::attr(href)").get()

# thumb_response = requests.get(URL_BASE + thumb_url)  # acessando a página
# book_selector = Selector(thumb_response.text)  # não esquecer do .text
# book_title = book_selector.css("div.product_main h1")  # não esquecer do get
# print(book_title.get())

# raspando os titulos com o for
for url in selector.css("div.image_container a::attr(href)").getall():
    thumb_response = requests.get(URL_BASE + url)
    book_selector = Selector(thumb_response.text)  # não esquecer do .text
    book_title = book_selector.css("div.product_main h1").get()
    print(book_title)
