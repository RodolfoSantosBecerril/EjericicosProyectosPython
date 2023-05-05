

class Color:
    def __init__(self, color):
     self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def __str__(self):
        return f'Color[color: {self._color}]'


class Tamano:
    def __init__(self,grande,mediano,pequeno):
        self.grande=grande
        self.mediano=mediano
        self.pequeno=pequeno
#generamos metodos get y set para grande
    @property
    def grande(self):
        return self._grande #._ para encapsulumiento
    @grande.setter
    def grande(self,grande):
        self._grande=grande # ._para encapsulamiento
#metodos get y set para mediano
    @property
    def mediano(self):
        return self._mediano #._para encapsulamiento
    @mediano.setter
    def mediano(self,mediano):
        self._mediano=mediano #._ para encapsulamiento
#metodos get y set para pequeno
    @property
    def pequeno(self):
        return self._pequeno
    @pequeno.setter
    def pequeno(self,pequeno):
        self._pequeno=pequeno
    def __str__(self):
        return f'figura grande, mediana, pequeña {self._Tamano}'

tam=Tamano('Grande ','medianao','pequeno')
print(tam.grande)