from mundo_pc.dispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones=0
    def __init__(self, marca, tipoEntrada):
        Raton.contadorRatones+=1
        self._id_raton=Raton.contadorRatones
        super().__init__(marca,tipoEntrada)
    def __str__(self):
        return f'id:{self._id_raton} Marca:{self._marca} Tipo de Entrada{self._tipoEntrada}'


if __name__ == "__main__":

 raton1=Raton('HP', 'USB')
 print(raton1)
 raton2=Raton('Acer','Bluetooth')
 print(raton2)