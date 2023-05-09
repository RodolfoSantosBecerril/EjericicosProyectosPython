#Funciones anidadas
def calculadora(a,b):
    #Funcion anidada
    def sumar(a,b):
        return a+b
    def restar(a,b):
        return a-b
#Mandamos a llamar la funcion anidada
    print(f'sumar: {sumar(a,b)}')
    print(f'restar: {restar(a,b) }')
calculadora(3,4)
