#profundizando en tipo str
import  math
from mi_clase import MiClase
#concatenando automatica
variable='adios'
mensaje='hola' 'mundo' #No es necesario poner + sin embargo no se puede concatenar asi las variables
mensaje1='hola mundo' + variable

print(mensaje)
print(mensaje1)

#help(str.capitalize) # Solicitar información de tipo str
#help(math.isnan)

'''
comentario 
de varias 
lineas 
'''

#help(MiClase)
print(MiClase.__doc__) #Solo definicion de clase
print(MiClase.__init__.__doc__)# Se recupera la documentacion del metodo init
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))

#help(str.capitalize)
mensaje1='hola mundo'
mensaje2=mensaje1.capitalize()
print(f'mensaje1: {mensaje1} id: {id(mensaje1)}')
print(f'mensaje2: {mensaje2} id: {id(mensaje2)}')

mensaje1 += ' adios'
print(f'mensaje1 :{mensaje1}, id: {hex(id(mensaje1))}')

tupla_str=('hola', 'mundo', 'desde', 'python')
mensaje= ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_frutas=["manzana", "mango","melon","naranja"]
mensaje=", ".join(lista_frutas)
print(f'mensaje: {mensaje}')

cadena ='HolaMundo'
mensaje=".".join(cadena)
print(f'mensaje:{mensaje}')

diccionario={'nombre':'Rodolfo', 'apellido':'Becerril', 'edad':'25'}
llaves="-".join(diccionario.keys())
valores="_".join(diccionario.values())
print(f'Llaves: {llaves}, type:{type(llaves)}')
print(f'valores:{valores}, type:{type(valores)}')

#help(str.split)

platillos='sopa taco tamal huevo pollo caldo' # De una cadena podemos convertila en lista
lista_platillos=platillos.split()
print(f'lista de platillos:{lista_platillos}')
print(type(lista_platillos))

platillos_separados_coma= 'sopa, taco, tamal, huevo, pollo, caldo'
lista_platillos=platillos_separados_coma.split(',  ')
print(f'lista de platillos separados por coma:{lista_platillos}')
print(lista_platillos)


lista_platillos=platillos_separados_coma.split(', ',2)
print(f'lista de platillos separados por coma:{lista_platillos}')
print(len(lista_platillos))


#Dar Formato a un str


nombre='Rodolfo'
edad=25
#Esto se conoce como porcentaje posicionales
mensaje_con_formato='Mi nombre es %s y mi edad es %d años'%(nombre, edad) #se mandan como tupla
print(mensaje_con_formato)

#Definiendo tupla desde el incio

persona=('rodolfo', 'santos', 5000.00)
mensaje_con_formato="hola %s %s. Tu salario es %.2f"%(persona)
print(mensaje_con_formato)
mensaje_con_formato='hola %s %s. Tu salario es %.2f'
print(mensaje_con_formato%(persona))

#Metodo format
nombre='Rodolfo'
edad=25
sueldo=3000
mensaje_con_formato='Nombre:{} Edad:{} sueldo:{:.2f}'.format(nombre,edad,sueldo)
print(mensaje_con_formato)

mensaje='Nombre: {0} Edad: {1} Sueldo: {2:.2f}'.format(nombre,edad,sueldo)
print(mensaje)


mensaje='Nombre--- {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje)

#como diccionario
diccionario={'nombre':'Rodolfo', 'edad':25,'sueldo':5000}
mensaje='Nombre: {dic[nombre]} Edad: {dic[edad]} Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)

#fstring o template literal

nombre='rodolfo'
edad=25
sueldo=30000
mensaje=f'Nombre{nombre} Edad {edad} sueldo{sueldo:.2f}'
print(mensaje)
#metodo print
print(nombre, edad, sueldo, sep=', puedes poner espacios comas etc') #Esto es una tupla








