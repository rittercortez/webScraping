from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# Extracion solo Vertical
class Hotel(Item):
    nombre = Field()
    descripcion = Field()
    comodidades = Field()

class Trip_Advisor(CrawlSpider):
    name = 'Scraping Vertical'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
    }
    start_urls = ['https://www.tripadvisor.com/Hotels-g187497-Barcelona_Catalonia-Hotels.html']

    download_delay = 2  # sirve para dar 2 segundos por cada consulta asi evitamos el baneo de nuestra IP

    # nos permite buscar una parte de la ruta relativa
    rules = (
        Rule(
            LinkExtractor(
                allow = r'/Hotel_Review-'
            ), follow=True, callback= "parsear_pagina"
        ),
    )
    def parsear_pagina(self,response):
        parsear = Selector(response)
        item = ItemLoader(Hotel(),parsear)
        item.add_xpath('nombre','//h1[@id="HEADING"]/text()')
        item.add_xpath('descripcion','//div[contains(@class,"_2f_ruteS _1bona3Pu")]/div/text()')
        item.add_xpath('comodidades','//div[contains(@class,"_1nAmDotd")]/div/text()')


        yield item.load_item()

