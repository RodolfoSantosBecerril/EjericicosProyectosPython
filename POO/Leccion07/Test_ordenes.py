from Orden import Orden
from Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalón', 150.00)
producto3= Producto('calcetin', 30.04)
producto4= Producto('blusa', 39.33)
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
orden1.agregar_producto(producto4)
orden1.agregar_producto(producto2)
orden1.agregar_producto(producto2)
orden1.agregar_producto(producto2)
orden1.agregar_producto(producto2)
orden1.agregar_producto(producto1)
print(f'Total de la orden 1: {orden1.calcular_total()}')
orden2 = Orden(productos2)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()}')
