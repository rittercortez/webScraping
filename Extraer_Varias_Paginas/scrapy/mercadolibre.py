from scrapy.item import Item
from scrapy.item import Field
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class extracion(Item):
    nombre = Field()
    precio = Field()
    descripcion = Field()

class mercadolibre(CrawlSpider):
    name = "Extracion Vertical y Horizontal"
    custom_settings = {

        'USER_AGENT':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
        'CLOSESPIDER_PAGECOUNT':6
    }
    download_delay = 1
    allowed_domains = ['computacion.mercadolibre.com.ar','articulo.mercadolibre.com.ar']
    start_urls = ['https://computacion.mercadolibre.com.ar/pc-escritorio/']

    rules = (
        # Este primer 'Rule' nos permite mover por las diferentes paginas
        Rule(
            LinkExtractor(
                allow= r'/pc-escritorio/pc/_Desde_'
            ),follow= True
        ),
        # Este segundo 'Rule' nos permite ya ejecutar el parseo para extraer datos
        Rule(
            LinkExtractor(
              allow= r'/MLA-'
            ),follow= True, callback= 'parse_page'
        ),
    )
    def limpieza(self,texto):
        texto = texto.replace('\n',' ').replace('\r',' ').replace('\t',' ').strip()
        return texto

    def parse_page(self, response):
        item = ItemLoader(extracion(),response)
        item.add_xpath('nombre','//h1[@class="ui-pdp-title"]/text()')
        item.add_xpath('precio', '//span[@class="price-tag-text-sr-only"]/text()')
        item.add_xpath('descripcion', '//p[@class="ui-pdp-description__content"]/text()'
                       ,MapCompose(self.limpieza))

        yield item.load_item()