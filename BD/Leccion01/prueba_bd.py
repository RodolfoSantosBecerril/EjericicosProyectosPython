import psycopg2

conexion= psycopg2.connect(user='postgres', password='admin',
                           host='127.0.0.1',
                           port='5432',
                           database='test_db')

""" Funcionamiento basico 
#print(conexion)
#cursor, ejecuta sentencias sql en posgrest
cursor=conexion.cursor()
sentencia='SELECT * FROM persona'
cursor.execute(sentencia)
registros=cursor.fetchall()
print(registros)

#cerrar conexion a base de datos

cursor.close()
conexion.close()
"""
""" #REGRESA TODOS LOS REGISTROS
try:
 with conexion:
     with conexion.cursor() as cursor:
         sentencia='SELECT * FROM Persona'
         cursor.execute(sentencia)
         registros=cursor.fetchall()
         print(registros)
except Exception as e:
    print(f'ocurrió un error {e}')
finally:
    conexion.close()
"""
 #REGRESA SOLO UN REGISTRO

"""
try:
 with conexion:
     with conexion.cursor() as cursor:
        #sentencia='SELECT id_persona, nombre   FROM persona' #Recuperando campos
        #sentencia = 'SELECT *  FROM persona WHERE id_persona=1' #Recuperamos el ID
        #sentencia = 'SELECT *  FROM persona WHERE id_persona=%s' #parametro posicional o placeholder
        #sentencia='SELECT * FROM persona WHERE id_persona IN (1,2,3,4)'
        sentencia = 'SELECT * FROM persona WHERE id_persona IN  %s'
        entrada=input('proporcina el id\´s a buscar (separados por comas):')
        #id_persona=input('Ingresa el valor de id_persona:')
        #id_persona=1
        #cursor.execute(sentencia,(id_persona,)) #id_persona debe tener "," para que se considere una tupla y no una variable
        llave_primarias=(tuple(entrada.split(',')),)
        cursor.execute(sentencia, llave_primarias)
        registros=cursor.fetchall() # fectchone solo regresa un registro
        for registro in registros:
          print(registro)
except Exception as e:
    print(f'ocurrió un error {e}')
finally:
    conexion.close()
"""
#Agregar persona con insert into
"""
try:
 with conexion:
     with conexion.cursor() as cursor:

      sentencia=  'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
      valores=('rodolfo','Jimenez','renompop@gmail.com')
      #conexion.commit() el comit se ejecuta dentro de whitch
      cursor.execute(sentencia,valores)
      registros_insertados= cursor.rowcount
      print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'ocurrió un error {e}')
finally:
    conexion.close()
"""
#Agregar varios registros
"""
try:
    with conexion:
     with conexion.cursor() as cursor:
      sentencia= 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
      valores=(('Rodolfo01','becerril01','possionblack@gmail.com'),
               ('Rodolfo02', 'becerril02', 'possionblack2@gmail.com'),
               ('Rodolfo03', 'becerril03', 'possionblack3@gmail.com'),
               )
      cursor.executemany(sentencia,valores) #pasamos la tupla con executemany pasamos todos los valores, con execute solo 1
      registros_insertados=cursor.rowcount
      print(f'Registros insertados: {registros_insertados}')
except Exception as e:
   print(f'Ocurrio un error {e}')
finally:
 conexion.close()
"""
#Actualizar  un registro
"""
try:
 with conexion:
     with conexion.cursor() as cursor:
         sentencia= 'UPDATE persona SET  nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
         valores=('rodolfo001', 'santos001','becerril001@gmail.com', 1)
         cursor.execute(sentencia,valores)
         registros_Acualizados=cursor.rowcount
         print(f'Registros Actualizados. {registros_Acualizados}')
         print()
except Exception as e:
    print(f'ocurrió un error {e}')

finally:
 conexion.close()
"""
#Actualizar varios registros
"""
try:
    with  conexion:
        with conexion.cursor() as cursor:
          sentencia='UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
          valores=(
              ('rodolfo001', 'santos001',  '1234@gmail.com',1),
              ('rodolfo002', 'santos002', '4567@gmail.com',2),
              ('rodolfo003', 'santos003', '8910@gmail.com',4)
          )
          cursor.executemany(sentencia, valores)
          registros_actualizados=cursor.rowcount
          print(f'Registros Actualizados: {registros_actualizados}')

except Exception as e:
    print(f'ocurrio un error: {e}')
finally:
    conexion.close()
"""
#Eliminar un solo registro
"""
try:
   with conexion:
       with conexion.cursor() as cursor:
           sentencia='DELETE FROM persona WHERE id_persona=%s'
           entrada=input('Ingresa el id_persona a eliminar:')
           valores=(entrada,)
           cursor.execute(sentencia, valores)
           registros_eliminados= cursor.rowcount
           print(f'Registros Eliminados: {registros_eliminados}')

except Exception as e:
    print(f'ocurrio un error')
finally:
    conexion.close()
"""
#Eliminar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia='DELETE FROM persona WHERE id_persona IN %s'
            entrada=input('Proporciona los id_persona a eliminar (separados por una coma):')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia,valores)
            registros_eliminados=cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()