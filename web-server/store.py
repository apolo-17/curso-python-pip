import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #el codigo de la respuesta http
    print(r.text) #contenido de la respuesta
    print(type(r.text)) #tipo de contenido de la respuesta
    categories = r.json()
    for category in categories:
        print(category['name'])
        