from mundo_pc.computador import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from orden import Orden
from teclado import Teclado

teclado1=Teclado('HP', 'USB')
raton1=Raton('HP', 'USB')
monitor1=Monitor('HP',15)
computadora1=Computadora('Hp', monitor1,teclado1,raton1)

teclado2 = Teclado('HP', 'USB')
raton2 = Raton('HP', 'USB')
monitor2 = Monitor('HP', 15)
computadora2 = Computadora('Hp', monitor2, teclado2, raton2)


teclado3 = Teclado('HP', 'USB')
raton3 = Raton('HP', 'USB')
monitor3 = Monitor('HP', 15)
computadora3 = Computadora('Hp', monitor3, teclado3, raton3)

computadora1=[computadora1,computadora2]
orden1=Orden(computadora1)
print(orden1)


orden1.agredarComputadora(computadora3)
print(orden1)

computadoras2=[computadora2,computadora3]
orden2=Orden(computadoras2)
print(orden2)