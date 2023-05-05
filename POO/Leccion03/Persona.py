class Persona1:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
#Definimos metodo para recuperar informacion
#Estamos sobre escribiendo el metodo de la clase padre desde la clase hija
    def __str__(self):
        return f'Persona: {self.nombre}: {self.edad}'

class Empleado1(Persona1):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        return  f'Empleado:[Sueldo: {self.sueldo}] {super().__str__()}]'

empleado1 = Empleado1('Reno', 22, 5500)
print(f'Nombre: {empleado1.nombre} edad: {empleado1.edad} sueldo: {empleado1.sueldo}')

class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return f'{self.nombre}: {self.edad}'

per=Persona('benito',3)
print(per.nombre)
print(per.edad)
class HerenciaPersona(Persona):
    def __init__(self,sueldo, nombre, edad):
        super().__init__(nombre,edad)
        self.sueldo=sueldo
    def __str__(self):
        return f'Empleado:[Sueldo: {self.sueldo}] {super().__str__()}]'
sueld=HerenciaPersona('Julia',20,100.99)
print(sueld.sueldo)

class Carro(HerenciaPersona):
    def __init__(self,nombre,edad, tipoCarro):
        super().__init__(nombre, edad, tipoCarro)
        self.tipoCarro=tipoCarro

    def __str__(self):
         return f'el Carro lo maneja: {self.nombre}  con edad: {self.edad} con carro de tipo: {self.tipoCarro}'
tipo=Carro('benito',22,'Pointer')

print(tipo.nombre)
print(tipo.tipoCarro)
print(tipo.edad)

###############Ejercixio

class Vehiculo:
    def __init__(self,color, ruedas):

     self.color=color
     self.ruedas=ruedas
    def __str__(self):
     return  f'color:{self.color}, ruedas de tipo:{self.ruedas}'
vehiculo=Vehiculo('rojo','de Vehiculo')
print(vehiculo)

class Coche(Vehiculo):
     def __init__(self,color, ruedas, velocidad):
      super().__init__(color,ruedas)
      self.velocidad=velocidad
     def __str__(self):
      return f'La velocidad es: {self.velocidad} Km/h [{super().__str__()}]'
coche=Coche('azul','de Coche',10)
print(coche)
class Bicicleta(Vehiculo):

    def  __init__(self,color,ruedas,tipo):
        super().__init__( color,ruedas)
        self.tipo=tipo
    def __str__(self):
        return f'tipo:{self.tipo}  [{super().__str__()}]'
bicicleta=Bicicleta('cafe','de bicicleta',' bici demontaña')
print(bicicleta)