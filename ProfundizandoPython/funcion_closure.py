#un closure es una funcion que define a otra y ademas la puede regresar
#la funcion anidada puede acceder a las variables locales
#En la funcion principal o externa

#funcion principal

def operacion1(a,b):
    #Definimos una funcion interna o anidada
    def sumar():
        return a+b
    #retornamos la funcion
    return sumar
mi_funcion_closure= operacion1(5,2)
print(f'Resultado de la funcion closure:{mi_funcion_closure()}')

#llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion1(2,3)()}')
def operacion(a,b):
    #1.Definimos una funcion lambda interna o anidada y la retornamos
    return lambda :a+b
mi_funcion_closure= operacion(5,2)
print(f'Resultado de la funcion closure:{mi_funcion_closure()}')

#llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(2,3)()}')


