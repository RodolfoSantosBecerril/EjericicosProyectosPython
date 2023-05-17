"""
List Comprehension en Python es una forma concisa y elegante de crear listas basadas en una expresión y un conjunto de iterables. Es una técnica poderosa que permite crear y manipular listas de manera eficiente en una sola línea de código.
La sintaxis básica de un List Comprehension es la siguiente:

"""

numeros=range(10)
lista_pares=[]

for numero in numeros:
    if numero % 2== 0:
        lista_pares.append(numero*numero)

print(f'lista pares: {lista_pares}')

#Hacemos lo mismo pero con list comprehensions
#[expresion for var in coleccion  if condicion]
#La condicion del if es opcional

lista_pares=[]
lista_pares=[numero*numero for numero in numeros if numero % 2==0]
print(f'lista de pares: {lista_pares}')

#Un ejemplo simila con dos conciones (las condiciones son opcionales=
#Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
#Es decir, debe ser divisible entre 2 y divisible entr 6

pare=[numero for numero in range(50) if numero % 2 == 0 if numero % 6 ==0]
print(f'Lista divisible entre 2 y 6: {lista_pares}')
#Agregando if else

lista_pares=[]
lista_impares=[]
for numero in range(10):
     if numero % 2 == 0:
       lista_pares.append(numero)
     else:
        lista_impares.append(numero)

print(f'Pares: {lista_pares}')
print(f'impares: {lista_impares}')

#El mismo ejercicio con lis comprehensions
lista_pares=[]
lista_impares=[]
[lista_pares.append(numero) if numero %2==0 else
lista_impares.append(numero) for numero in range(10)]

print(f'Pares: {lista_pares}')
print(f'impares: {lista_impares}')

