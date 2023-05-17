#Definimos una varaible global
contador=0

def mostar_contador():
    print(contador)
def modificar_contador(c):
    global contador
    contador=c

modificar_contador(5)
mostar_contador()

