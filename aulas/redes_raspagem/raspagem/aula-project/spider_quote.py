import requests
from parsel import Selector


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return response.status_code
    else:
        return response.text


print(fetch_content("http://httpbin.org/status/404"))


def extract_quotes(text):
    seletor = Selector(text)
    quotes = []
    for quote in seletor.css("div.quote"):
        # raspando o texto da citação
        text = quotes.css("div.quote")
        # raspando o nome do autor
        author = quote.css("span.text::text").get()
        # raspando o nome da tag
        tags = quote.css("a.tag::text").getall()
        quotes.append({"text": text, "autor": author, "tags": tags})
    return quotes


def all_quotes():
    base_url = "http://quotes.toscrape.com"
    next_page = "/"
    quotes = []
    while next_page:
        content = fetch_content(base_url + next_page)
        quotes.extend(extract_quotes(content))
        next_page = Selector(content).css("li.next > a::attr(href)").get()
