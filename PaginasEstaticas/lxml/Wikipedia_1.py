


import requests
from lxml import html
"""
    "user-agent :" se utiliza para que las WEBS no nos detecten como su fueramos ROBOTS e introducimos una dirección 
               como si accedieramos desde un equipo original

"""

encabezado = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
}


"""
    "requests.get" : utilizamos la libreria requests para hacer la pregunta al servidor Web indicandole la URL y 
                     nuestro "user-agent" para evitar que nos banee el servidor
    "headers ="    : se utiliza para introducir el encabezado que seria nuestro "user-agent"
"""
url =  "https://www.wikipedia.org/"
requests = requests.get(url, headers = encabezado)

############ Parser  (lxml) #############
"""
    "html.fromstring()" : lo vamos a utilizar para parsear la estructura html
    ".get_element_by_id()" : se utiliza para extraer datos de "id"
    ".text_content()" : permite mostrar el contenido en formato texto
"""
parser = html.fromstring(requests.text)



#### Extraer Datos Especificos ####

# Opcion 1: id especifico  (lxml)
extraccion_id_lxml = parser.get_element_by_id("js-link-box-es")
print(extraccion_id_lxml.text_content())

# Opcion 2: id especifico (XPath)
"""
    'xpath()' : nos permite extraer el contenido de la etiqueta 'a' atravez del atributo
                '@id=' la ruta nos lleva a la etiqueta hijo 
                'strong' que la convertimos en texto para poder visualizarlo
"""
extraccion_xpath = parser.xpath("//a[contains[@id = 'js-link-box-es']]/strong/text()")
print(extraccion_xpath)



##### Extraer Multiples datos  ####
# OPCION 1 (XPath)
idiomas_xclass = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
for idiomas in idiomas_xclass:
    print(idiomas)
    
# OPCION 2 (lxml)
idiomas_lclass = parser.find_class('central-featured-lang')
for idiomas in idiomas_lclass:
    print(idiomas.text_content())




