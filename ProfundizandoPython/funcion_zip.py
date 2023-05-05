# print(dir(__builtins__)) imprime las calses y metodos disponibles en python
# help(zip)
numeros = [1, 2, 3, 4]
letras = ['a', 'b', 'c', 'd']
identificadores = 303, 404, 301, 340, 405, 540
conjunto = {3, 35, 67, 8, 98}  # Al momento de enviar no se guarda el orden
# el set no respeta el orden
mezcla = zip(numeros, letras, identificadores, conjunto)
print(mezcla)  # debemos ponerlo en lista
print(list(mezcla))  # En modo de lista
print(tuple(zip(numeros, letras)))  # En modo de tupla
print(type(mezcla))
# con la funcion zip puedo recorrer varios iterables al mismo tiempo

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Numero: {numero}, letras: {letra}, id: {id}, aleatorio: {aleatorio}')

nueva_lista = []

for numero, letra, id, aleatorio in zip(numeros, letras, identificadores, conjunto):
    nueva_lista.append(f'{id}--{numero}--{letra}--{aleatorio}')
print(nueva_lista)

#Efecto unzip no hay una funcion directa para unzip
mezcla=[(1,'a'),(2,'b'),(3,'c')]
numeros, letras= zip(*mezcla) #para unpaking se antepone un *
print(numeros, letras)

#ordenar un zip
letras=['c','f','r','a','b','e']
numeros=[3,4,5,0,2,1]
mezcla=zip(letras,numeros)
#imprimiendo sin ordenar
print(tuple(mezcla))
#Ordenar por letra
print(sorted(zip(letras,numeros)))
#El primer iterador ocupa el orden
print(sorted(zip(numeros,letras)))

#crear un diccionario zip y dos iterables
llaves=['Nombre','Apellido','Edad']
valores=['rodoflo','santos',25]
#creamos el diccionario con la clase dict
diccionario=dict(zip(llaves,valores))
print(diccionario)
#Pueden ser tuplas o valores

#Actualizar un elemento de un diccionario
#llave=['edad'] # se agrega una nueva llave
llave=['Edad']#se actualiza esta llave
nueva_edad=[26]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)


