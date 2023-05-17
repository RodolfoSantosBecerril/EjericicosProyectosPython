#Funciones anidadas
def calculadora(a,b, operacion="sumar"):
    #Funcion anidada
    def sumar(a,b):
        return a+b
    def restar(a,b):
        return a-b
#Mandamos a llamar la funcion anidada
    if  operacion =="sumar":
     print(f'sumar: {sumar(a,b)}')
    elif operacion =="restar":
     print(f'restar: {restar(a,b) }')
calculadora(3,4)
calculadora(2,3, operacion="restar")

