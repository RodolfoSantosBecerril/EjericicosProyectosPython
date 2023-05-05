from mundo_pc.dispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contadorTeclados =0
    def  __init__(self, marca,tipoEntrada):
      Teclado.contadorTeclados += 1
      self._id_teclado=Teclado.contadorTeclados
      super().__init__(marca,tipoEntrada)
    def  __str__(self):
        return f'id:{self._id_teclado} Marca:{self._marca} Tipo de Entrada:{self._tipoEntrada}'

if __name__=='__main__':
 teclado1 = Teclado('teclado HP','USB' )
 print(teclado1)
 teclado2 = Teclado('Teclado Sonny','Bluetooth' )
 print(teclado2)
