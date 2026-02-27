# Listas

listas = [60, 10, 20, 30, 40, 50]

# AÑADIR RECURSOS A LA LISTA
listas.append(60)
listas.insert(0, 100)

# OBTENER UN ELEMENTO MEDIANTE INDICE
print(listas[0])

# IMPRIMIR TODOS LOS ELEMENTOS DE MI LISTA
print(listas)

# ELIMINAR ELEMENTOS

listas.remove(60)
elemento_eliminado = listas.pop(0)

print(listas)
print(elemento_eliminado)

# ACTUALIZAR ELEMENTOS

listas[0] = 10000
listas[4] = 20000

print(listas)