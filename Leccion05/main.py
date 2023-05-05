"""
nombres = ['Rodolfo','manuel','benito', 'reno']
print(nombres)
#acceder a los elementos de la lista
print(nombres[0])
print(nombres[1])
print(nombres[2])
#Elementos en forma inversa
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) #El espacio numero 3 no se incluye
print(nombres[:3])#todos menos el cuarto
print(nombres[1:])#Todos menos el primero
nombres[3]='Yun' #Cambiarmos un valor de la lista
print(nombres)
for nombre in nombres:
     print(nombre)
else:
    print("Ya no hay mas nombres")
#Preguntar el largo de una lista
print(len(nombres))
nombres.append('Santos')#Agregamos un nuevo elemento en la lista
nombres.insert(1,'mari')#Agrefamos un nuevo elemento en el indice proporcionado
print(nombres)
nombres.remove('mari')#Remover elemento por valor
print(nombres)
nombres.pop() #Elimina el ultimo valor de la lista
print(nombres)
del nombres[0]#Se elimina un indice
print(nombres)
nombres.clear()#limpia  la lista
print(nombres)
#del nombres   #se elimina toda la lista
#print(nombres)

#iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
print("iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3")
for num in range(11):
    if(num%3==0):
        print(num)
#Imprimiendo un rango de numeros de 2 a 6
print("Rango de 2 a 7, inicio en 2 y fin en 6")
rango=range(2,7)
for i in rango:
    print(i)
print("Rango de 3 a 10 pero con incrementos de 2")
ran=range(3,11,2) # definimos el incremento agregando una coma y el numero a incrementar
for i in ran:
    print(i)
#En una tupla no se puede agregar mas elementos
frutas =('naranja', 'melon', 'sandia')
print(frutas)
print(len(frutas)) #saber el rango
print(frutas[0])#acceder a un elemento
print(frutas[-1])#ponerlos de forma inversa
print(frutas[0:1])#del primero hasta el 1
print(frutas[0:2])#del primero hasta el 2
print(frutas[0:3])#del primero hasta el 3
print(frutas[0:])#del primero hasta el ultimo
print(frutas[:2])#hasta 2
#Recorrer elementos
for fruta in frutas:
    print(fruta, end=' ') #sin saltos de linea, agregamos el elemento de end

#cambiar valor de tupla
frutasLista=list(frutas)  #Cambiamos de tupla a lista por medio de list y se la agregamos a una nueva variable
frutasLista[0]='pera'     #asignamos el valor en el elemento dado
frutas=tuple(frutasLista) #volvemos a convertin a una tupla
print('\n',frutas)

#CONSIDERAR QUE ES UN TIPO UNMUTABLE no se puede modificar
#No se puede agragar elemento ni modificarlos.
#pero una tupla si se puede eliminar
#del frutas
#print(frutas)

###########################set##################
#no mantiene orden y no se pueden modificar

print('''


''')
planetas= {'marte', 'jupiter', 'tierra'}
print(planetas)
print(len(planetas))
print( 'marte' in planetas) #Preguntar si marte esta en planetas
planetas.add('pluton')#agregar nuevo elemento
print(planetas)
#no se pueden duplicar elementos, nos puede servir para no agregar duplicados
#planetas.add('pluton')

#eliminar elementos con error
planetas.remove('tierra')
print(planetas)
#eliminar elementos sin arrojar error
planetas.discard('martes')
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
#print(planetas)
"""
diccionario={
    'IDE':'integrated development environment',
    'OOP':'object oriented programming',
    'DBMS':'database management system'
}
print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemnto (key)
print(diccionario['IDE'])
print(diccionario.get('OOP'))
#Modificar elementos
diccionario['IDE']='Integrated Development Environment MODIFICADO'

print(diccionario)
for termino, valor in diccionario.items(): #para mostrar dos variables utilizamos  el metodo items
    print(termino, valor)
for termino in diccionario.keys():#regresa solo la llave
    print(termino)
for valor in diccionario.values():#solo el valor de la llave
    print(valor)
print('IDE' in diccionario) #comprobar si ya existe un elemento
#agregar un elemento
diccionario['PK']='primary key'
print(diccionario)
#remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#eliminar el diccionari
#del diccionario
print(diccionario)
""" ##########################ENTRENAMIENTO

#Crear una tupla que solo incluya numero menores a 5
tupla=(13,1,8,3,2,5,8)
#Definimos la lista que guardará los datos
lista=[]
for elemento in tupla:
     if elemento<5:
         lista.append(elemento) #agregamos los elementos a la lista
print(lista)

tup=(12,3,4,5,6,6,77,7,8,6,4,4,44,4,5,5,6,3,2,2)
lista1=[]
for i in tup:
  if i<10:
      lista1.append(i)
print(lista1)

tuplita=(1,2,3,4,5,6,7,8,9)
#guardamos la tupla en una lista vacia
listaTuplita=[]
 #iteramos los elementos de la lista y la guardamos en una variable
for i in tuplita:
 if i<10:
  listaTuplita.append(i) #agrefamos elemento a la lista
print(listaTuplita)

tupla=(2,3,4,5,6,5,4,3,2,1,2,3,4,5,6,6)
#guardamos la tupla en una lista vacia
listaVacia=[]
#iteramos los elementos
for i in tupla:
    if i <7:
        #agregamos los elementos a la lista vacia
     listaVacia.append(i)
#imprimimos cada elemento de la lista ya creada
print(listaVacia)


definirtupla=(1,2,3,4,5,6,7,5,2,2,3,4,3,3,3,3,3,3,3,3,3,3,)
#guardar tupla en lista
lis=[]
for i in definirtupla:
 if i==3:
     #guadamos los elementos en la lista
    lis.append(i)

print(lis)
print(len(lis))
print(len(definirtupla))
"""