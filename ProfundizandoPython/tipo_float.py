#profundizando en el tipo float
a=3.0

print(f'a:{a:.2f}') #imprimir valores es interpolación
#Constructor float puede recibir int y str
a=float(10)
print(f'a:{a:.2f}')
a=float('10')
print(f'a:{a:.2f}')
#Notación exponencial (valores positivos o negativos)
a=3e5
print(f'a:{a:.2f}')
a=3e-5
print(f'a:{a:.5f}') #ver valor hasta 5 decimales
#Cualquier calculo de tipo float se vuelve todo a float
a=4.0+5
print(a)
print(type(a))

