import utils as utl

data = [{
  'Country': 'Colombia',
  'Population': 500
}, {
  'Country': 'Bolivia',
  'Population': 300
}, {
  'Country': 'Peru',
  'Population': 200
}]


def run():
  keys, values = utl.get_population()
  print(keys, values)

  country = input('Type Country >= ')
  result = utl.population_by_country(data, country)
  print(result)

## este if le dice al archivo main.py que si es ejecutado desde 
# la terminal, ejecute el metodo run
# Se le llama: Entry point
if __name__ == '__main__':
  run()
