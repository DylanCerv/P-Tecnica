# Un usuario quiere saber cuánto dinero necesita para comprar todos los stocks disponibles, ( solo necesitamos el dato )

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


import certifi
import json


def get_data(url):
    """Recibir el contenido de 'url', se analisa como JSON y se devuelve el objeto.
        Parametros
        ----------
        url : str

        Return
        -------
        dict
    """
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)



list_stocks = ['AAPL','GOOGL','AMZN','TSLA','FB','TWTR','UBER','LYFT','SNAP','SHOP']

p = 0
for i in list_stocks:
    url = "https://financialmodelingprep.com/api/v3/quote-short/"+i+"?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22"

    value = get_data(url)
    p += value[0]['price']


print(p)



# Un usuario quiere saber con X dinero (ejemplo 3 millones USD) cómo sería su portafolio, invirtiendo en las empresas 
# con acciones de mayor valor optimizando el valor mínimo restante ( que sobre la menor cantidad de dinero ).
#
# - El usuario debe invertir en todas las acciones listadas
# - La solución puede ser cli / rest / lo que sea más cómodo


for i in list_stocks:
    url = "https://financialmodelingprep.com/api/v3/quote-short/"+i+"?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22"

    value = get_data(url)
    print(value)
