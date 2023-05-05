#Profundizar en set
#Un set es una colección de elementos unicos #
#Además un set es Mutable
#Pero los elementos de un set deben ser INMUTABLE
#conjunto={[1,2,3],[4,5]}
conjunto={'Rodolfo','Santos',True, 10.4}
print(conjunto)
#conjunto={} eso no es un set vacio, esto es un diccionario
#set vacio CORRECTO
conjunto=set()
print(conjunto)
print(type(conjunto))
#un set es mutable
conjunto.add('Becerril')
print(conjunto)

#Un set contiene elementos unicos
conjunto.add('Becerril')
print(conjunto)
#los sets no se duplican,siempre vamos a tener valores diferentes

#Crear un set a partir de un iterable
conjunto=set([4,4,7,7,1,2])
print(conjunto)
# no contiene elementos duplicados
#Podemos agregar más elemento o incluso otro set
conjunto2={100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)
conjunto_copia=conjunto.copy()
print(conjunto_copia)
#Copiar un set (de manera poco profunda)
#solo se copia las referencias.
#un set no guarda el orden
#Verificar la igualdad de los dos set
print(f'Es el mismo contenido?{conjunto==conjunto_copia}')
print(f'Es igual la referencia?: {conjunto is conjunto_copia}')

#operacion de conjuntos con set
#personas con distintas carecteristicas
pelo_negro={'rodolfo','rodolfo1','rodolfo2'}
pelo_rubio={'rodolfo4','rodolfo3','Rodolfo5'}
ojos_cafe={'rodolfo','rodolfo2','rodolfo3'}
menores_30={'rodolfo1','rodolfo2','rodolfo3'}
#union de ojos cafe y pelo rubio
print(ojos_cafe.union(pelo_rubio))
#invertir el orden con el mismo resultado (conmutativo)
print(pelo_rubio.union((ojos_cafe)))

#interseccion (solo las personas con ojos cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
#también es conmutativa
print(pelo_rubio.intersection(ojos_cafe))
#Diferencia entre dos set
#pelo negro sin ojos color cafe
#se encuantran en el primer set  pero no en el tercer set
print(pelo_negro.difference(ojos_cafe))
#Diferencia simetrica
#Regfresa todos los elementos excepto las coincidencias en el set
#diferencia simetrica pelo negro u ojos café, pero No ambos (conmutativa)
print(pelo_negro.symmetric_difference(ojos_cafe))
