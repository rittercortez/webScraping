from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy. loader import ItemLoader
from scrapy.crawler import CrawlerProcess

# Esta es la clase que definimos que se encarga de extraer la información
class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()

# Esta clase servira para hacer requerimientos y pasear la pagina
# 'Spider' es un atributo que nos permite hacer estraciones de UNA SOLA PAGINA
class Pagina_spider(Spider):
    # Le ponemos nombre a nuestra extracción
    # 'custom_settings' acompañado de 'USER_AGENT' se utiliza en scrapy para evitar que nos pueda banear el servidor
    # al hacer consultas
    name = "Mi primera extración con Scrapy"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    # introducimos nuestra url general
    start_urls = ["https://stackoverflow.com/questions"]
    #Está funcion parse la utilizaremos tal y como la vemos aqui para parsear
    def parse(self,response):
        # 'Selector' nos permite parsear o hacer un selector en nuestro scrapy
        selector = Selector(response)
        preguntas = selector.xpath('//div[@id="questions"]//div[@class="summary"]')
        # recorremos nuestra ruta mas relativa para que nos de información uno por uno de cada caja summary

        for pregunta in preguntas:
            # 'ItemLoader'  esta clase nos permite cargar nuestra ruta la cual le queremos sacar informacion y enviarla
            # a nuestra clase Pregunta
            item = ItemLoader(Pregunta(),pregunta)
            # 'add_xpath' esta funcion la utilizamos para ejecutar comandos xpaths en nuestro scrapy
            item.add_xpath('pregunta','.//h3/a/text()')
            #item.add_xpath('descripcion','.//div[@class="summary"]/text()')
            #item.add_value('id',1)

            # 'yield' se utiliza para retornar el valor cargado de nuestros item
            yield item.load_item()

