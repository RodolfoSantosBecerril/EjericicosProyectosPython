"""operandoA=3
operandoB=4
suma=operandoA+operandoB
print("resultado de la suma es", suma)
print(f"Resultado suma: {suma} ") #f de format es lo mas usado

resta=operandoA-operandoB
print(f"Resultado de resta: {resta}")

mult=operandoA*operandoB
print(f"Resultado de multiplicacion: {mult}")

div=operandoA/operandoB
print(f"Resultado de division: {div}")
#division de tipo entero
div=operandoA//operandoB
print(f"Resultado de division: {div}")

modulo=operandoA%operandoB
print(f"Resultado del residuo o modulo {modulo}")

exponente= operandoA** operandoB
print(f"Resultado del exponente {exponente}")


alto=int(input("ingresa el alto:" ))
ancho=int(input("ingresa el ancho"))
res=(alto*ancho)
per=(alto+ancho)*2
print(f"El area es: {res}")
print(f"el perimetro es: {per}")
"""
"""
miVariable=10
print(miVariable)
miVariable=miVariable+1
print(miVariable)

miVariable+=1
print(miVariable)

miVariable*=30
print(miVariable)

miVariable=miVariable+1
print(miVariable)

miVariable/=2
print(miVariable)
miVariable= miVariable/3
print(miVariable)

a=4
b=2
res=(a==b)
print(f'resultado comparacaicon ==: {res}')

res= (a!=b)
print(f'resultado comparacaicon !=: {res}')

res= (a>b)
print(f'resultado comparacaicon >: {res}')

res=(a >= b)
print(f'resultado comparacaicon >=: {res}')

res= a < b
print(f'resultado comparacaicon <: {res}')
res= a <= b
print(f'resultado comparacaicon <=: {res}')

a = int(input('Escribe un valor numérico: '))

print(a % 2)
if a % 2 == 0:
    print(f'El valor de a {a} es número par')
else:
    print(f'El valor de a {a} es número impar')
#Usar comillas simples
 
numero= int(input('ingresa un numero: '))
if (numero >=18) :
     print(f'Tu edad es: {numero} y eres mayor de edad')
else:
     print(f'Aun no eres mayor de edad: {numero}')

a=True
b=False
res= a and b
print(res)

res= a or b
print(res)
#cambia de cierto a falso 
res= not a
print( res)

valor = int(input("Ingresa un numero: "))

if valor >= 0 and valor <= 5:
    print(f'EL valor {valor} está dentro del rango')

else:
    print(f'No esta en rango {valor}')


vacaciones= True
diasDescanso=False

if not(vacaciones or diasDescanso):
    print(" No se puede asistir")
else:
    print("Se puede asistir")

edad = int(input("Ingresa tu edad: "))

if edad<=20 or edad<=30:
    print("cierto")
else:
    print("Falso")


valor=int(input("ingrese  su edad: "))
veinte= valor >=20 and valor <=29
print(veinte) #De esta manera se si es cierto o falso
treinta=valor >=30 and valor <=39
print(treinta)

if veinte or treinta:
    if veinte:
        print("Estas en tus 20\'s")
        print(valor)
    elif treinta:
        print("Estas en tus 30\'s")
        print(valor)

else:
    print("No estas en rango")

valor=int(input("ingresa el valor 1: "))
valor2=int(input("ingresa el valor 2: "))
if valor>valor2:
    print(f'el numero 1 es mayor')
else:
    print(f'el numero 2 es mayor')
"""
