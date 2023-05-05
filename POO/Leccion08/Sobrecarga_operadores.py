
class Persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def __add__(self, other):
        return f'  {self.nombre}  {other.edad}'
    def __sub__(self, other):
        return  self.edad -other.edad
persona1= Persona('renowq',2)
persona2=Persona('renowq', 54)

print(persona1+persona2)
print(persona1-persona2)