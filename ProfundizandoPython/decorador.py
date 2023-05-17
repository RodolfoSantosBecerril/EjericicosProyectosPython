# Decoradores
# Un decorador es una función que recibe una función y regresa una función (al menos)
# Lo utilizamos para extender funcionalidad de una función
# 1. Función decorador (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)
def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes desde la función_decorada_c')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después desde la función decorada_c')
        return resultado
    return funcion_decorada_c


# Definimos una función y vamos a extender su funcionalidad con un decorador
@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostrar_mensaje')

# Ejecutamos la función a decorar
mostrar_mensaje()

@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')

imprimir()

@funcion_decorador_a
def sumar(a,b):
    return a+b

resultado=sumar(5,6)
print(f'Resultado de la suma: {resultado}')