from  Cuadrado import Cuadrado, Muestra
from  Color import  Tamano
from  Rectangulo import Rectangulo
print('Creacion de objeto cuadrado' .center(50,'-'))
cuadrado1=Cuadrado(5,'rojo')
#print(cuadrado1.ancho)
#print(cuadrado1.alto)
#print(cuadrado1.color)
#print(cuadrado1.calcular_area())

#MRO =Method Resolution Order
#print(Cuadrado.mro()) # Se manda a llamar el orden de las llamadas a las clases

print(cuadrado1)
print('Creacion de objeto rectangulo' .center(50,'-'))
rectangulo1=Rectangulo(ancho=5, alto=3, color='verde') # Estamos atocomentando
print(rectangulo1)
print(f'Calcular el area del Rectangulo:{rectangulo1.calcular_area()}')
print('Orden de llamada a las clases ' .center(50,'-'))
print(Rectangulo.mro())
print('calcular area cuadrado' .center(50,'-'))
calcular=Cuadrado(lado=5, color='rojo') # Estamos atocomentando
calcular.alto=2
calcular.ancho=9
print(calcular)
print(calcular.calcular_area())
print('Pruebas reno' .center(50,'-'))
tam2=Tamano('mediano','pequeno','grande')
print(tam2.grande)
print(tam2.mediano)
print(tam2.pequeno)
print('Ejemplo de herencia' .center(50,'-'))
imprimir=Muestra(lado=2,color="rojo",funciona="si")
print(imprimir)
