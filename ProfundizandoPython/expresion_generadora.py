#Expresion Generadora (Es un generador anonimo)
multiplicacion =(valor*valor for valor in range(4))
print(multiplicacion)
print(type(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#podemos pasar una expresion generadora a una funcion (sin usar parentesis)
import math
suma=sum(valor*valor for valor in range(4))
print(f'resultado de la suma: {suma}')

#Tambien podemos usar una lista o cualquier otro iterador

lista=['Rodolfo','Santos']
generador=(valor for valor in lista)
print(f'Expresion generadora: {next(generador)}')
print(f'Expresion generadora: {next(generador)}')

#Crear un string a partir de un generador creado o partir de una lista

lista=['Rodolfo', 'Santos']
contador=0
#Definimos una funcion para incrementar la variable
def incrementar():
  global contador
  contador +=1
  return contador
  #la primera parte es el yield del generador
  #la segunda es el for, entre parentesis
generador=(f'{incrementar()}, {nombre} ' for nombre in lista)
#Creamos una lista
lista=list(generador)
print(lista)
cadena=', '.join(lista)
print(f'Cadena generada: {cadena}')

