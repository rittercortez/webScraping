from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class Cine(Item):
    titulo = Field()
    puntuacion = Field()
class Tv(Item):
    titulo = Field()
    fecha = Field()

class Tech(Item):
    titulo = Field()
    descripcion = Field()

class ign(CrawlSpider):
    name = "IGN SPAIN"
    # custom_settings  nos permite evitar que nos baneen nuestra IP los servidores webs
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
        'CLOSESPIDER_PAGECOUNT': 30
    }
    # allow_domains =  nos permite agregar dominios de la pagina para no obtener mas informacion de la realmente necesaria
    allowed_domains = ['es.ign.com']
    # Introducimos nuestra URL la principal
    start_urls = ['https://es.ign.com']
    # Aqui vamos a declarar las reglas de busquedas en la paginacion
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/preview/'
            ),follow = True, callback ='parse_preview'
        ),
        Rule(
            LinkExtractor(
                allow=r'/video/'
            ),follow = True ,callback = 'parse_tv'
        ),
        Rule(
            LinkExtractor(
                allow= r'/news/'
            ),follow = True ,callback = 'parse_tech'
        ),
    )
    def parse_preview(self,response):
        item = ItemLoader(Cine(),response)
        item.add_xpath('titulo','//h1/text()')
        item.add_xpath('puntuacion','//span[@sclass="side-wrapper side-wrapper hexagon-content"]/text()')

        yield item.load_item()
    def parse_tv(self,response):
        item = ItemLoader(Tv(),response)
        item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
        item.add_xpath('fecha', '//span[@class="publish-date"]/text()')

        yield item.load_item()
    def parse_tech(self,response):
        item = ItemLoader(Tech(),response)
        item.add_xpath('titulo', '//h1[@id="id_title"]/text()')
        item.add_xpath('descripcion', '//div[@id="id_text"]//*/text()')

        yield item.load_item()
