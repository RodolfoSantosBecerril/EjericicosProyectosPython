class Persona:
 mi_atributo=''
#metod init es en constructor agregamos atributos y los inicializamos
 def __init__(self):   #self pasa la referencia a self
     self.nombre='Reno'
     self.apellido='Becerril'
     self.edad=28
 def mostarDetalle(self):
     print(f'Persona:{self.nombre} {self.apellido} {self.edad}')
persona1=Persona() #Se crea un objeto y se manda a llamar
persona1.mostarDetalle()
persona1.telefono='2334455'
print(persona1.telefono)
persona2=Persona()
persona2.mostarDetalle()
#print(type(Persona))
print(persona1.nombre)
print(persona2.nombre)
print(persona1.edad)
print(persona1.apellido)

class Per:
    def __init__(self,nombre,apellido,edad, ):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
personaEjemplo=Per('reno','becerril',23, )
print(personaEjemplo.nombre)
print(personaEjemplo.apellido)
print(personaEjemplo.edad)
persona2=Per('Reno2','Becerril2',46)#creando otro objeto
print(f'objeto persona2: nombre- {persona2.nombre} apellido- {persona2.apellido} edad- {persona2.edad}')


class Ejemplo:
    def __init__(self, nombre, apellido, edad, *args,**kywords):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.args=args
        self.kywords=kywords
    def mostrarDetalle(self):
        print(f'nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}, tupla: {self.args}, mediante Diccionarios: {self.kywords}')

ejemploPersona=Ejemplo('rodolfo', 'becerril', 23,  12, 12, 4, 54, m='manzana', mel='melon', s='sandia'  )
ejemploPersona.mostrarDetalle()

#---------------------------------------------------------------------------------ENCAPSULAMIENTO, GET Y SET--------------------------------------------------
class GetterSetter:
    def __init__(self,nombre, apellido):
        self._nombre=nombre
        self.apellido=apellido
    @property
    def nombre(self):
        print("Ejecutando get")
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        print("Ejecutando set")
        self._nombre=nombre
    def mostrarDetalle(self):
        print(f'nombre: {self.nombre} --- apellido: {self.apellido}')
objeto=GetterSetter('Rodolfo','Santos')
print(objeto.nombre)
objeto.nombre='Rodolfo MODIFICADO'
print(objeto.nombre)

class GetySetPractica:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self._apellido=apellido
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre=nombre
    def mostrar(self):
        print(f'nombre: {self.nombre} y apellido: {self.apellido}')

objeto=GetySetPractica('Benito','Fernandez')
print(objeto.nombre)
objeto.nombre="nombre Modificado"
print(objeto.nombre)


class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')
    def __del__(self): ##Destructor
        print(f'Persona: {self.nombre} {self.apellido}')
if __name__== '__main__':
 persona1 = Persona('Juan', 'Perez', 28)
 persona1.nombre = 'Juan Carlos'
 persona1.apellido = 'Lara'
 persona1.edad = 30
 persona1.mostrar_detalle()
 print(__name__)
