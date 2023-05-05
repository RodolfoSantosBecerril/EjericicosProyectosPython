from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self,nombre,sueldo,puesto):
        super().__init__(nombre,sueldo)
        self.puesto=puesto

    def __str__(self):
        return f'{super().__str__()} puesto:{self.puesto}  '