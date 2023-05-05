class Monitor:

     contadorMonitor=0
     def __init__(self, marca, tamaño):
         Monitor.contadorMonitor +=1
         self._id_monitor=Monitor.contadorMonitor
         self._marca=marca
         self._tamaño=tamaño

     def  __str__(self):
      return  f'id:{self._id_monitor} Marca:{self._marca} Tamaño:{self._tamaño}'


if __name__=='__main__':
 monitor1=Monitor('Sonny',12)
 print(monitor1)
 monitor2=Monitor('HP',15)
 print(monitor2)