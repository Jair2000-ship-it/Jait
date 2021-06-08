esto_es_una_string="Angie"
esto_es_otra_string="mundo"

#concatenar
print(esto_es_una_string + ''+ esto_es_otra_string)
#hola mundo

#MAYUS
print(esto_es_una_string.upper())
#minus
print(esto_es_una_string.lower())
#primero en mayus
print(esto_es_una_string.capitalize())
#pone en mayus la primera letra de cada palabra
print(esto_es_una_string.title())
#me dice la longitud
print(len(esto_es_una_string))

#buscar una caracter y muestra su ubicacion
print(esto_es_una_string.find('e'))

#rebanar
print(esto_es_una_string[0:2]) #ho tu le dices que inicio
print(esto_es_una_string[:2]) #asume que inicia en 0
print(esto_es_una_string[5:9])

#radar
variable = 'Angie'
print(variable[::])
print(esto_es_una_string[::-1])