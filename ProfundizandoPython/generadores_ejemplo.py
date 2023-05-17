#Definiendo un generador de numeros del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print(f'Se reanuda la ejecucion de la funcion')

#Usamos el generador
generador=generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

#obteniendo los valores del generador

for valor in generador:
    print(f'Numero producido en el generador:{valor}')

#Consumir a demanda
#Debemos llamar de nuevo al generador para consumirlo
generador=generador_numeros()
try:
 print(f'Consumimos a demanda:{next(generador)}')
 print(f'Consumimos a demanda:{next(generador)}')
 print(f'Consumimos a demanda:{next(generador)}')
 print(f'Consumimos a demanda:{next(generador)}')
 print(f'Consumimos a demanda:{next(generador)}')
except StopIteration as e:
    print(f'Error al consumir el generador {e}')

#Otra forma de consumir el generador

for valor in generador:
    print(f'Nuevo producto: {valor}')

generador=generador_numeros()
while True:
    try:
        valor=next(generador)
        print(f'Impresion valor generado: {valor}')
    except StopIteration as e:
        print('Se termino de la iterar el generador')
        break

