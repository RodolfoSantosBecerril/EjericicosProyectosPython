#las funciones en python son ciudadanas de primera clase
#Fris class citizens


#definimos la funcion
def sumar(a,b):
    return a+b
#asignar una funcion a una variable No se usan parentesis

mi_funcion=sumar

#Verificar el tipo de la variable
print(type(mi_funcion))
#llamamos la función atraves de la varible

#Llamamos a traves de la variable

resultado=mi_funcion(4,5)
print(f'resutlado: {resultado}')
#podemos asignar las funciones a las variables

#2--------Pasar funcion como argumento

def operacion(a,b, sumar_arg):
    print(f'resultado de sumar: {sumar_arg(4,5)}')
operacion(3,4, sumar)

#podemos regresar una funcion desde otras funciones
def retornar_funcion():
    #retornarmos una funcion
    return sumar
mi_funcion_retornada=retornar_funcion()
print(f'Resultado funcion retornada: {mi_funcion_retornada(6,7)}')

