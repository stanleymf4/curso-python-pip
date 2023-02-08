import requests

def get_category():
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  print(r.status_code)
  print(r.text)
  print(type(r.text))
  categories = r.json() #Transformar en un formato json para obtener la lista y poder iterar
  for category in categories:
    print(category['name'])