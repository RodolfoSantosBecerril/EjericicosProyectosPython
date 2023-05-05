#debug
""""
condi = True

if condi == True :
     print('verdadero')
elif condi == False:
     print("Falso ")
else:
     print("condicion no reconocida")

numero=int(input("Ingresa un valor entre 1 y 3: "))

if numero==1:
    numeroTexto='Uno'
elif numero==2:
    numeroTexto="Dos"
elif numero== 3:
     numeroTexto="tres"
else:
    numeroTexto="valor fuera de rango"
print(f'numero es: {numero}:  -- {numeroTexto} ')
"""

calif=int(input("Ingrese una calificacion: "))
if 9<= calif<=10:
    print("A")
elif 8<=calif<9:
    print("B")
elif 7<=calif<=8:
    print("C")
elif 6<=calif<7:
    print("D")
elif 0<=calif<=5:
    print("F")
else:
    print("valor incorrecto")
