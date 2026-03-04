# Diccionarios

# CREACION DE UN DICCIONARIO

paises_capitales = {
    'Mexico': 'CDMX',
    'España': 'Madrid',
    'Paris': 'Francia',
    'Italia': 'Roma'
}

# OBTENER UN ELEMENTO DE UN DICCIONARIO USANDO 'INDEX VALUE'

capital_mexico = paises_capitales['Mexico']


# OBTENER UN ELEMENTO DE UN DICCIONARIO USANDO 'get()'

capital_espania = paises_capitales['España']


# TRATAR DE OBTENER UNA KEY Y SI NO EXISTE COLOCAR UN VALOR POR DEFECTO

capital_no_encontrada_pero_hay_valor_por_defecto = paises_capitales.get('Chile', 'no existe')


# INSERTAR UN NUEVO ELEMENTO EN EL DICCIONARIO

paises_capitales['Chile'] = 'Santiago de Chile'


# ELIMINAR UN ELEMENTO DE UN DICCIONARIO CON 'INDEX VALUE'

del paises_capitales['Chile']


# ELIMINAR UN ELEMENTO DE UN DICCIONARIO USANDO 'pop()'

paises_capitales.pop('Italia')


# TRATAR DE ELIMINAR UN ELEMENTO QUE NO EXISTE Y REGRESAR UN VALOR POR DEFECTO

capital_no_eliminada_pero_hay_valor_por_defecto = paises_capitales.pop('Ecuador', 'no eliminado')


# ACTUALIZAR EL VALOR DE UNA KEY QUE EXISTE EN EL DICCIONARIO

paises_capitales['Italia'] = 'la key existe y se cambio el valor, no es un INSERT'





