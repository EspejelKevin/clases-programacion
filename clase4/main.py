class ConsumirAPIError(Exception):
    def __init__(self, msg):
        super()


def consumir_api_externa(fecha):
    print('consumiendo una api externa')
    return {'message': 'la reserva del producto IM-1234563-0'}

resultado = None

try:
    print('extrayendo un valor de tienda virtual')
    valor_de_tienda_virtual = ['fecha de hoy']

    fecha = valor_de_tienda_virtual[0]

    resultado = consumir_api_externa(fecha)

    if not resultado:
        raise ConsumirAPIError('no se pudo consumir la api externa de cadena de suministro')

except ConsumirAPIError as ex:
    print('log error:', ex)
    resultado = {'data': {'mensaje': 'la reservacion no se hizo correctamente', 'status_code': 500}}
finally:
    print('respuesta enviada al frontend')

    if resultado:
        print('log info: se ejecuto la reserva')

    print(resultado)
