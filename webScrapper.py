import requests
from bs4 import BeautifulSoup

url = 'https://miportal.entel.cl/personas/catalogo/celulares'

# Realizar la solicitud HTTP al sitio web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:

    # Parsear el contenido HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # Encuentra los elementos que contienen los datos de los celulares
    celulares = soup.find_all('div', class_='team__item')

    # Iterar a través de los elementos y extraer la información deseada
    for celular in celulares:
        nombre = celular.find('h2', class_='team__name').text.strip()
        precio = celular.find('p', class_='team__charge').text.strip()
        print(precio)
        print(f'Nombre: {nombre}')
        print(f'Precio: {precio}')
        print('---')
else:
    print(f'Error al hacer la solicitud. Código de estado: {response.status_code}')

