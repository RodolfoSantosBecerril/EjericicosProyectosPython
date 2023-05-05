#profundizando en listas
#las listas son mutables
nombres1=['Rodolfo','Santos','Becerril']
nombres2='RODOLFO SANTOS BECERRIL'.split()

#Sumar listas con +
print(f'Sumasr listas{ nombres1+nombres2}')
#extender una lista con  otra lista
nombres1.extend(nombres2)
print(f'Extender lista 1 {nombres1+nombres2}')

#listas de numeros
numeros1=[10,30,50,52,40]
print(f'Lista original: {numeros1}')
#regresa el primer elemento encotrado en una lista
#help(list.index)
print(f'indice 4: {numeros1.index(40)}')
#invertir el orden de los elementos de una lista
numeros1.reverse()
print(f'lista invertida: {numeros1}')
#ordenar los elementos de una lista
numeros1.sort() #Ordena los elementos de menor a mayor
print(f'Lista ordenada de manera ascendente:{numeros1} ')
#ordenando de manera  descendente una lista
numeros1.sort(reverse=True)
print(f'Lista ordenada de manera descendente: {numeros1}')

#obtener el valor minimo y maximo de una lista
print(f'Valor minimo: {min(numeros1)}')
print(f'Valor máximo: {max(numeros1)}')

#Copiar los elementos de una lista
numeros2=numeros1.copy()
#help(list.copy)
print(f'Misma referencia de memoria? {numeros1 is numeros2}')
print(f'Tienen el mismo contenido? {numeros1==numeros2}')

#Slicing para copiar elementos
numeros2= numeros1[:]
print(f'Misma referencia de memoria? {numeros1 is numeros2}')
print(f'Tienen el mismo contenido? {numeros1==numeros2}')

#Multiplicación de listas
lista_multiplicacion=5*[[2,5]]
print(lista_multiplicacion)
#hacer esto tiene la misma referencia en memoria
print(f'Misma referencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Misma contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10) #Modificamos el objeto del indice 2 los demas elementos se copian
print(lista_multiplicacion)

#Matriz en python
matriz=[[10,20],[30,40,50],[60,70,80,90]]
print(f'Matriz original:{matriz}')
print(f'Recuperar renglon 0, Columna 0 : {matriz[0][0]}')
print(f'Recuperar renglon 2, Columna 2 : {matriz[2][2]}')
print(f'Recuperar renglon 2, Columna 3 : {matriz[2][3]}')
matriz[2][0]=65
print(f'Matriz modificada{matriz}')

lista_listas=[[10,23,45,6,7],[2,3,4,5],[36,3,2,3,45,6]]
lista_listas.sort(key=len)
print(f'lista ordenada por cantidad de elementos: {lista_listas}')
#sorted built-in Función incorporada en python
#help(sorted)
frutas1=['manzana','mango','arandano' ,'sandia','melon','platano']
frutas1=sorted(frutas1, reverse=True)
print(frutas1)
#podemos ordenar por la cantidad del largo de los caracteres
frutas1=sorted(frutas1, key=len)
print(frutas1)
#A diferencia de sort(), sorted() no modifica la lista original, sino que devuelve una nueva lista ordenada.

#built-in reversed
frutas1=reversed(frutas1)
#print(frutas1)#debemos convertirlo a una lista
print(list(frutas1))

