import requests
from random import randint

url = 'https://api.mercadolibre.com/sites/MLA/search'
args = {'q':'televisor philips 55'}

response = requests.get(url,params=args)

print(response)

if (response.status_code == 200):

    response_json = response.json()
    print('Cantidad Total de la Búsqueda: ')
    num = int(response_json['paging']['total'])
    print(num)
    num_random = randint(0,50)
    print('-----')
    #obtengo un item al azar
    item_random = response_json['results'][num_random]

    id_del_item_random = item_random['id']
    print('Id del Item al azar: '+id_del_item_random)
    moneda_publicacion = item_random['currency_id']
    print('Moneda del Item al azar: ' + moneda_publicacion)
    precio_publicacion = item_random['price']
    print('Precio del Item al azar: ' + str(precio_publicacion))
    mercado_pago_publicacion = item_random['accepts_mercadopago']
    print('Acepta Mercado Pago el Item al azar: ')
    print(mercado_pago_publicacion)
    ##################################################################################
    #Aca obtengo los datos del item random

    url_item = 'https://api.mercadolibre.com/items'
    args_item = {'id': id_del_item_random}

    response_item = requests.get(url_item, params=args_item)
    if (response_item.status_code == 200):
        response_json_item = response_item.json()
        print('Comparación del precio de publicacion y del item:')
        print(precio_publicacion == response_json_item['base_price'])
        print('Comparación de las monedas publicacion y del item:')
        print(moneda_publicacion == response_json_item['currency_id'])
        print('Comparación acepta mercado pago de publicacion y del item:')
        print(mercado_pago_publicacion == response_json_item['accepts_mercadopago'])
