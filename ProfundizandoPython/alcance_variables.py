#Tiempo de vida de variables
#Alcance de Variable (scope)
var_global = 'Variable Global'

def imprimir():
    #Acceder a una variable global
    global var_global
    print(f'Variable global desde funcion: {var_global}')
    #variable local
    var_local="variable local"
    print(f'Variable local desde función: {var_local}')
    var_global="nuevo valor de variable global"
    print(var_global)
    def funcion_anidada():
        print(f'Variable local dentro dentro de funcion anidada: {var_local}')
        funcion_anidada()
        print(var_global)

imprimir()
print(f'variable global fuera de la funcion: {var_global}')
#print(f'Variable local fuera de la funcion definida: {var_local}')

