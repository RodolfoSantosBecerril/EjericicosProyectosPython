# mi_funcion() No se puede utilizar la funcion antes de usarla
"""
def mi_funcion(nombre, apellido):  # Definir es importar la funcion
    print("hola desde mi funcion")
    print(f'nombre:{nombre} apellido:{apellido}')


mi_funcion('rodolfo', 'santos')
mi_funcion("reno", "renin")


def sumar(a, b):
    return a + b


resultado = sumar(4, 5)
print(resultado)
print(f'Resultado de la suma es: {resultado}')
# se puede mandar a llamar la funcion directamente
print(f'Resultado de la suma es: {sumar(4, 5)}')  # no es necesario una variable extra

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
listaTupla = []
for i in tupla:
    if i <= 5:
        listaTupla.append(i)
print(listaTupla)
print(len(listaTupla))
print(len((tupla)))
listaTupla.clear()


# print(listaTupla)

def listarNombres(*nombres):  # en la documentacion se puede econtrar como *args
    for nombre in nombres:
        print(nombre)


listarNombres('reno', 'reno1', 'reno2')
listarNombres('reno3', 'reno4')


def sumaVariable(*args):
    res=0
    for valor in args:
        res=res+valor
    return res
print(sumaVariable(1, 2, 3, 4, 5, 6, 7, 8))

def multiplicacionVariable(*args):
    res=1
    for valor in args:
        res=res*valor
    return res
print(multiplicacionVariable(1, 2, 3, 4, 5, 6, 7, 8))

#se puede poner en el argumento varios argumentos
#como argumento variable y con argumento variable con llave
# def listarTerminos(nombres, *nombres, **terminos)
def listarTerminos(**terminos): # **kwargs iterar un diccionario:
    for llave, valor in terminos.items():
     print(f'{llave}........{valor}')
listarTerminos(IDE='Integrated Developement Environment', PK='Primary Key')
listarTerminos(DBMS='Database Management System')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres=['reno','reno1','reno2']

desplegarNombres(nombres) #
desplegarNombres('reno') #Iteracion caracter por caracter
desplegarNombres((3,4))#lo reconoce como tupla
desplegarNombres([5,6])#lo reconoce como lista

def factorial(numero):
 if numero==1:
    return  1
 else:
     return numero*factorial(numero-1)
numero=5
res=factorial(numero)
print(f'El factorial de {numero} es: {res}')

"""
"""
def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print ("\nFallaste! Inténtalo de nuevo" )
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print ("\nPerdiste!")
    else:
        print("\nGanaste!")
jugar()
"""
"""
def funcionRecursiva(conteo):
    if conteo == 1:
       return 1
    else:
        return conteo*factorial(conteo-1)
conteo=5
res=funcionRecursiva(conteo)
print(f'El resultado es: { res}')

def funcionRecu(conta):
    if conta==1:
        return 1
    else:
        return conta*funcionRecu(conta-1)
conta=5
resu=funcionRecu(conta)
print( resu)

def funcionDesendiente(conteo):
    if conteo>=1:
     print(conteo)
     funcionDesendiente(conteo-1)
    elif conteo==0:
     return
    elif conteo<=0:
     print("valor incorrecto")

funcionDesendiente(13)
"""
def funcion(num1,num2):
     return num1+num2*(num1/100)

num1=float(input("ingresa un numero"))
num2=float(input("ingresa un numero"))
print(funcion(num1,num2))

