#Podemos desempacar el contenido de una variable
numeros=[1,2,3]
print(numeros)
#en lugar de que se muestre como lista se muestan los elementos
print(*numeros)
print(*numeros,sep=' Espacio ')
#**kwargs  para desempaquetar diccionarios es con doble *

#desempaquetando al momento de pasar un parámetro a una función
def sumar(a,b,c):
    print(f'Resultado de la suma:{a+b+c}')
sumar(*numeros)

#Extraer algunas partes de una lista o cualquier iterable
mi_lista=[1,2,3,4,5,6]
a,*b,c,d=mi_lista #la variable b toma los valores restantes
print(a,b,c,d)

#unir listas
lista1= [1,2,3]
lista2=[4,5,6]
lista3=[lista1,lista2]
print(f'lista de listas: {lista3}')
lista3=[*lista1,*lista2] #desempaquetar los elementos, es una sola lista
print(f'lista unida: {lista3}')
#también se puede unir diccionarios, unir diccionarios
dic1={'papa':1,'arroz':2,'maiz':3}
dic2={'frijol':4,'elote':5}
dic3={**dic1,**dic2}
print(f'unir diccionario:{dic3}')
#como construir una lista a partir de un str
lista=[*'HolaMundo']
print(lista)
print(*lista, sep='') #para no imprimir espacios agregamos el operador vacio
