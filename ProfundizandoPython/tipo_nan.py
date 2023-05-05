import  math
from decimal import Decimal
#NoN-Not a number (No es un numero)
#NoN no es sensible a mayusculas/minusculas
a=float('NaN')
print(f'a:{a}')
print(f'Es Nan (not a numbrer)?: {math.isnan(a)}')
a=Decimal('Nan')
print(f'a: {a}')
print(f'Es Nan (not a number)?: {math.isnan(a)}')
