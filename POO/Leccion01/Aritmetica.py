

class Aritmetica:

  def __init__(self, operandoA, operandoB): #en lugar de self puede ser this
      self.operandoA = operandoA
      self.operandoB = operandoB
  def sumar(self):
      return self.operandoA + self.operandoB

aritmetica1 = Aritmetica(23,3)
print(f'Suma: {aritmetica1.sumar()}')

class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB, operandoC):
        self.operandoA = operandoA
        self.operandoB = operandoB
        self.operandoC = operandoC

    def sumar(self):
        return self.operandoA + self.operandoB + self.operandoC
    def restar(self):
        return  self.operandoA - self.operandoB - self.operandoC
    def multiplicar(self):
        return self.operandoA * self.operandoB * self.operandoC
    def divir(self):
        return  self.operandoA/ self.operandoB /self.operandoC


aritmetica1 = Aritmetica(5,3,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'resta: {aritmetica1.restar()} ')
print(f'multiplicar: {aritmetica1.multiplicar()}')
print(f'dividir: {aritmetica1.divir()}')

class Uno:


    def __init__(self,auto,moto,bici):
        self.auto = auto
        self.moto = moto
        self.bici = bici

    def costo(self):
        return self.auto+self.moto+self.bici

costoTotal=Uno(12,23,1)
print(f'El resultado de sumar auto, moto y bici es: {costoTotal.costo()}')

class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    def formula(self):
        return self.altura* self.base
dato1=int(input("ingresa la base: "))
dato2=int(input("ingresa la altura: "))
datos=Rectangulo(dato1,dato2)
datos1=Rectangulo(dato1,dato2)
print(f'EL area del cubo es: {datos.formula()}')

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))
#Reutilizando el metodo creamos un nuevo objeto

rectangulo2 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo2.formula()}')
