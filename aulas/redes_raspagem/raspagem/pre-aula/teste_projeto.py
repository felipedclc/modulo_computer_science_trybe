from re import split
import requests
from parsel import Selector

url1 = "https://www.tecmundo.com.br/amp/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
url2 = "https://www.tecmundo.com.br/ciencia/226968-planta-amazonica-misteriosa-finalmente-identificada-meio-seculo.htm"
url3 = "https://www.tecmundo.com.br/minha-serie/215168-10-viloes-animes-extremamente-inteligentes.htm"
url4 = "https://www.tecmundo.com.br/dispositivos-moveis/215327-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm"
url5 = "https://www.tecmundo.com.br/seguranca/215274-pmes-principais-alvos-ataques-ciberneticos.htm"
url6 = "https://www.tecmundo.com.br/novidades"
response = requests.get(url=url1)
# print(response.url)
selector = Selector(response.text)
# print(selector.css("time::attr(datetime)").get())
# print(selector.css("a.tec--author__info__link::text").get().strip())
shares_count = 0
if selector.css(".tec--toolbar__item::text").get() is not None:
    shares_count = selector.css(".tec--toolbar__item::text").get().split()[0]
# print(shares_count)
# print(int(shares_count) if shares_count else 0)
first_p = "".join(
    selector.css("div.tec--article__body > p:nth-child(1) ::text").getall()
)
# print(first_p)
sel = "div.tec--article__body-grid > div.z--mb-16.z--px-16 > div > a"
# print([fonte.strip() for fonte in selector.css(f"{sel}::text").getall()])
# print([fonte.strip() for fonte in selector.css("div.z--mb-16 .tec--badge::text").getall()])

comments_count = selector.css("#tecAuthorBar > nav > button").get()
# print(comments_count)
# print(selector.css("head > link[rel=canonical]::attr(href)").get())


writer = (
    # selector.css("a.tec--author__info__link::text").get() or
    # selector.css("#tecAuthorBar > div > p:nth-child(1) strong::text").get()
    # selector.css(".tec--timestamp__item.z--font-bold a::text").get()
    selector.css(".z--truncate.z--font-bold::text").get()
)
# print(writer)

# req 3 -------------------------------------------------------------
# print(selector.css("a.tec--card__title__link::attr(href)").getall())

# req4 -----------------------------------------------------------------
next_page_url = "?page=1"
while next_page_url:
    next_page_url = selector.css("a.z--mx-auto.z--mt-48::attr(href)").get()
    # print(next_page_url)

comments_count = (
    selector.css(".tec--btn span.z--mr-4::text").get() or
    selector.css("button#js-comments-btn::attr(data-count)").get()
)
print(comments_count)
