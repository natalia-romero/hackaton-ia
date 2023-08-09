import requests
import csv
from bs4 import BeautifulSoup

# Archivo destino
archivo_destino = "../txt/telefonos.txt"
texto = 'El inventario consiste de:\n'

responses = []
start: int = 0
end: int = 24

# Obtener datos desde el dataset
print("Obteniendo datos desde el portal entel...")
while end < 96:
    # Request HTTP
    url = f'https://miportal.entel.cl/personas//catalogo/celulares?No=' \
          f'{start}&Nrpp={end}&contentPath=%2Fpages%2Fstorechilepp' \
          f'%2Fcatalogo%2Fcelulares&eIdx=8&sIdx=1&subPath=main%5B1%5D&format=json-rest'
    response = requests.get(url)
    response_json = response.json()
    responses.append(response_json["response"]["records"])

    start += 24
    end += 24

print("Datos obtenidos, generando CSV...")

# Obtener datos de los telefonos
for response in responses:
    for objeto in response:
        atributos = objeto["attributes"]
        marca = atributos["brand"][0]
        nombre = atributos["displayName"][0]
        precio = atributos["price.formatted"][0]
        almacenamiento = atributos["internal"][0]
        pantalla = atributos["product.screenSize"][0]
        camara = atributos["primary"][0]

        texto += f'Telefono {nombre}, Marca {marca}, Precio {precio} CLP, Almacenamiento {almacenamiento}, ' \
                 f'Pantalla de {pantalla} pulgadas, Camaras de {camara} megapixeles\n'

# Escribir csv
with open(archivo_destino, "w") as archivo:
    # Escribir el texto en el archivo
    archivo.write(texto)

print("Archivo TXT generado exitosamente.")
