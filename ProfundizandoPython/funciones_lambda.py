#funciones lambda
#Son funciones anonimas y pequeñas
#son solo una linea de codigo
#no es posible asignar una funcion a una varible
#def sumar(a,b): return a+b

#COn una funcion lambda (anonimo, sin nombre, y una sola linea de codigo)
#No se necesita agregar parentesis para los parametros
#No se necesita usar la palabra return, pero si debe regresar una expresion

mi_funcion_lambda=lambda a,b: a+b

resutlado = mi_funcion_lambda(4,5)
print('Resultado de funciones lambda', resutlado)

#funcion lamda que no recibe argumentos pero debemos regresar una expresion valida

mi_funcion_lambda=lambda: 'Funcion sin agumentos'
print(f'LLamar funcion lamda sin argumentos')

#Funcion lamda con parametros por default
mi_funcion_lambda=lambda a=2,b=3: a+b
#despues de los dos puntos lo toma con return
print(f'agumentos por defautl:{mi_funcion_lambda()}')

#Puedes pasar tuplas o diccionarios Argumentos variables

mi_funcion_lambda=lambda  *args, **kwargs: len(args)+len(kwargs)
print(f'Resultado de argumentos variables: {mi_funcion_lambda(1,2,3,4,a=3,b=5,c=9)}')
#Funcion lambda con argumentos variables y por default

mi_funcion_lambda= lambda  a, b, c=3,*args,**kwargs:a+b+c+len(args)+len(kwargs)
print(f'Resultado de funcion lambda: {mi_funcion_lambda(1,2,3,4,5,e=2,f=4)}')

