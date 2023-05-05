# unpacking o desempaquetado en python
valores = 1, 2, 3
print(valores)
print(type(valores))

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)
# si utilizamos _ es para saber que no vamos a usar esa variable
valor1, _, valor3 = 1, 2, 3
print(valor1, valor3)
# si pones un * todos los demas valores se guardan en el valor 3 en forma de lista

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6
print(valor1, valor2, valor3)

valor1, *valor2, valor3 = 1, 2, 3, 4, 5, 6
print(valor1, valor2, valor3)
print(type(valor2))
#considerando como lista
*valor1, valor2, valor3 = [1, 2, 3, 4, 5, 6]
print(valor1, valor2, valor3)
print(type(valor1))

def regresa_varios_datos():
    return (1,2,3) #tupla

valor1,valor2,valor3=regresa_varios_datos()
print(valor1,valor2,valor3)

valor1, *valores_restantes=regresa_varios_datos() #valores_restantes lo convierte a listas
print(valor1, valores_restantes)

#help(str.partition)
variable='17:20'.partition(':')
print(type(variable))
#separador
hora,_,minutos='17:20'.partition(':')
print(hora, minutos)
