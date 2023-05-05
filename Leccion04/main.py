"""
contador =0
while contador <= 10:
    print(contador)
    contador=contador+1

else:
    print("Fin")


contador=20
while contador>=1:
    print(contador)
    contador=contador-1
else:
    print("Fin ")

cadena="hola mundo"
for letra in cadena:
    print(letra)
else:
    print("fin")

"""

for letra in 'cadena':
    if letra == 'a':
        print(f'letra ya encontrada: {letra}')
        break
    else:
        print("fin ciclo")
else:
    print("fin")

for i in range(10):
    if i % 2 !=0:
        continue
    print(f'valor: {i}')