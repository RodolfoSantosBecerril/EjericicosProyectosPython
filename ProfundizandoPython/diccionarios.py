#profundizando en diccionarios
#Los diccionarios guardan el orden a diferencia de un set
# Produndizando en diccionarios

# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Rodolfo','Apellido':'Becerril','Edad':25}
print(diccionario)

# Los dic son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor1'}
# diccionario = {(1,2):'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario (si ya existe se reemplaza)
diccionario['Nombre'] = 'Rodolfo Santos'
print(diccionario)

#Recuperar un valor indicando una llave
print(diccionario['Nombre'])
#Si no encuentra la llave lanza una excepcion
#print(diccionario['nombre'])

#Método get recupera una llave y si no existe No lanza excepciones
#Además podemos agregar un valor en caso de que no exista la llave
print(diccionario.get('Nombre1', 'No se encontró la llave'))
print(diccionario)#No se modifica el diccionario
#setdefault si modifica el diccionario, además se puede agregar un valor por default
nombre=diccionario.setdefault('NombreModificado','Valor por default')
print(nombre)
print(diccionario)

#Imprimir pprint
from  pprint import pprint as pp
#help(pp)
pp(diccionario, sort_dicts=False)


