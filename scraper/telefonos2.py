import requests
import csv
from bs4 import BeautifulSoup

# Archivo destino
archivo_csv = "../csv/telefonos2.csv"
headers = ["marca", "nombre", "precio", "almacenamiento", "pantalla", "camara", "selfie"]

responses = []
start: int = 0
end: int = 24

# Obtener datos desde el dataset
print("Obteniendo datos desde el portal entel...")
while end < 168:
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

telefonos = []
# Obtener datos de los telefonos
for response in responses:
    for objeto in response:
        atributos = objeto["attributes"]
        marca = atributos["brand"]
        nombre = atributos["displayName"]
        precio = atributos["price.formatted"]
        almacenamiento = atributos["internal"]
        pantalla = atributos["product.screenSize"]
        camara = atributos["primary"]
        selfie = atributos["secondary"]

        telefono = {
            "marca": marca,
            "nombre": nombre,
            "precio": precio,
            "almacenamiento": almacenamiento,
            "pantalla": pantalla,
            "camara": camara,
            "selfie": selfie
        }
        telefonos.append(telefono)

# Escribir csv
with open(archivo_csv, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(telefonos)

print("Archivo CSV generado exitosamente.")
