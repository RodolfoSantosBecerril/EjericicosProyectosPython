#profundizando en tuplas
#Declaramos variables a,b
a,b ='Hola','Adios'
print(a,b)
a,b= b,a
print(a,b)

#Regresar multiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)
min,max=minmax([1,2,3,4,5,6]) #separamos
print(f'valor minimo:{min}, valor maximo:{max}')
#Regresa la suma de una tupla
resultado= sum((1,2,3,4,5))
print(f'Resulatado={resultado}')

def sumar(*args):
    return sum(args)
resultado=sumar(1,2,3,4,5,6,7)
print(f'Resultado:{resultado}')

