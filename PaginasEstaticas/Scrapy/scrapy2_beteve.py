from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy. loader import ItemLoader

class Preguntas(Item):
    preguntas = Field()
    descripcion = Field()

class MiSpider(Spider):
    name = "beteve"
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    start_urls = ["https://beteve.cat/societat/20-maig-2021-directe-coronavirus-catalunya-govern-mesures-anticovid/"]
    def parse(self, response):
        selector = Selector(response)
        cajas = selector.xpath('//div[@id="minut-a-minut-content"]//div[@class="element-minut-a-minut pt-3 mt-3"]')
        for caja in cajas:
            item = ItemLoader(Preguntas(),caja)
            item.add_xpath('preguntas','.//div[@class="column right"]/h3/text()')
            item.add_xpath('descripcion', './/div[@class="column right"]/p/span/text()')
            yield item.load_item()
