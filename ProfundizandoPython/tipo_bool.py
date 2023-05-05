#bool contiene los valores de True y False
#Tipos numericos, False para 0, True demás valores
valor=0.0
resultado=bool(valor)
print(f'Valor:{valor}, Resultado:{resultado}')
valor=15
resultado=bool(valor)
print(f'Valor:{valor}, Resultado:{resultado}')
#true para cualquier valor
valor=15
resultado=bool(valor)
print(resultado)
#Tipo str, False para '', True  para demas valores
valor=''
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor = 'Hola'
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

#Tipó de colecciones, False para colecciones Vacias, Ture para las demás colecciones
#lista
valor=[]
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor=[1,2,3,4]
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
#Tupla
valor=()
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor=(1,2,3,4)
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
#crear un diccionario
valor={}
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
valor= {'nomnbre:Rodolfo','apellido:Becerril'}
resultado=bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')
variable=[1] #puede asignar numeros, listas, tuplas, string etc..
if bool(variable):
    print('regresa verdadero')
else:
    print('regresa falso')
if '':
    print('Regresa verdadero')
else:
    print('Regresa falso')
while variable:
    print('ejecutando ciclo while')
    break

else:
    print('Fin del cilco')
