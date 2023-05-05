from FiguraGeometrica import FiguraGeometrica
from Color import Color
#Si queremos renombrar ponemos "as nombrenuevaclase"
class Cuadrado(FiguraGeometrica, Color ):
    def __init__(self,lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    def calcular_area(self):
        return self.alto*self.ancho
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}' #self para llamar la referencia
class Muestra(FiguraGeometrica,Color):
    def __init__(self, lado, color,funciona):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        self.funciona=funciona
    def __str__(self):
     return f'Clase Figura Geometrica: {FiguraGeometrica.__str__(self)} Clase Color:  {Color.__str__(self)}  Clase Funciona: {self.funciona}'

