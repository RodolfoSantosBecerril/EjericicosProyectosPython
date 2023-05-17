#mas funciones anidadas y alcance de variables
def funcion_externa():
    variable_local_externa="variable local externa"

    def funcion_anidada():
        variable_local_anidada="variable local anidada"

        nonlocal variable_local_externa
        variable_local_externa="Nuevo valor modificado con nonlocal"

    funcion_anidada()
    print(f'valor variable local externa :{variable_local_externa}')
    #No es posible acceder a una variable local mas interna
    #print(f'valor variable local anidada: {variable_local_anidada}')
funcion_externa()




