import requests
from bs4  import BeautifulSoup

# user-agent para protegernos del baneo 
user_agent = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
}

# La pagina de la que queremos extraer datos
url =  "https://stackoverflow.com/questions"

# La petición requests al servidor de la pagina, aqui introducimos la url y la protección del baneo
requests = requests.get(url, headers = user_agent)

# Parseamos la pagina o creamos la sopa de etiquetas para acceder luego
soap = BeautifulSoup(requests.text)

# Buscamos el atributo 'id' que no se repite por las cuales queremos acceder aqui seria buscar las etiquetas 
# padre y sus hijos luego para acceder a las etiquetas generales si queremos varia información de la misma caja.
cont_list = soap.find('div',id = "questions") 
mult_list = cont_list.find_all('div',class_="question-summary")

# Iteramos por nuestra variable 'mult_list' q 
for caja in mult_list:
    # Buscar la etiqueta a la cual le queremos sacar la pregunta en este caso cogemos la etiqueta h3 
    # por el unico motivo de que no se repite sino podriamos buscar por atribut
    pregunta = caja.find('h3').text
    respuesta = caja.find('div',class_="excerpt").text
    respuesta = respuesta.replace('\n','').replace('\r','')
    print(pregunta)
    print(respuesta)
    print()