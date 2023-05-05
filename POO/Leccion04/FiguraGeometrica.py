class FiguraGeometrica:
    def __init__(self, alto, ancho):
#validaciones de las clases
      if self._validarValor(ancho):
          self._ancho = ancho

      else:
          self._ancho=0
          print(f'valor erroneo: {ancho}')
      if self._validarValor(alto):
          self.alto=alto
      else:
          self.alto=0
          print(f'valor erroneo : {alto}')
#COmienza get
    @property
    def ancho(self):
     return self._ancho
#ejecuta set
    @ancho.setter
    def ancho(self, ancho):
        if self._validarValor(ancho):
         self._ancho = ancho
        else:
         print(f'Valor erroneo del ancho: {ancho} ')
#ejecuta get
    @property
    def alto(self):
     return self._alto
#ejecuta set
    @alto.setter
    def alto(self, alto):
        if self._validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo del alto: {alto} ')

#Metodo para sobre escribir para direccion de memoria object e imprimir nuestro texto
    def __str__(self):
        return f'Figura Gometrica [Alto:{self.alto}, Ancho:{self.ancho}]'
    def _validarValor(self,valor):
      return  True if 0< valor <10 else False