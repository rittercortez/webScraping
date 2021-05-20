from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy. loader import ItemLoader
from bs4 import BeautifulSoup

class Preguntas(Item):
    titulo = Field()
    descripcion = Field()

class MiSpider(Spider):
    name = "beteve"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    start_urls = ["https://beteve.cat/societat/20-maig-2021-directe-coronavirus-catalunya-govern-mesures-anticovid/"]
    def parse(self, response):
        global descripcion
        soap = BeautifulSoup(response.body)
        ruta = soap.find_all("div", class_="element-minut-a-minut pt-3 mt-3")
        for noticia in ruta:
            item = ItemLoader(Preguntas(),response.body)
            titulo = noticia.find('h3').text
            descripcion = noticia.find('p').text
            item.add_value('titulo',titulo)
            item.add_value('descripcion',descripcion)
            yield item.load_item()



