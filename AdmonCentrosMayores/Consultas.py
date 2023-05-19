from Conex.Conexion import Conexion
from datetime import datetime
class Consultas:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo Consultas creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   CONSULTAS')
            print('===============')
            print('0. Regresar')            
            print('1. Listado de Adultos Mayores por Centro')
            print('2. Listado de Actividades')
            print('3. Calificación de Actividades')
            print('4. Listado de Inscritos en Actividad')
            print('5. Actividades realizadas')
            print('5. listado de actividades realizadas en un centro específico')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Consultas")
            elif opcion == 1:
                self.verAlgo1()
            elif opcion == 2:
                self.verAlgo2()
            elif opcion == 3:
                self.verAlgo3()
            elif opcion == 4:
                 self.verAlgo4()
            elif opcion == 5:
                self.verAlgo5()
            elif opcion == 6:
                self.verAlgo6()
            else:
                print('Esa opción NO existe..!!!')
            input ()
            
    def verAlgo1 (self):
        try:
            center = input('Que centro desea ver?')
            mycursor=self.miConexion.cursor()
            query = 'SELECT centros.nombre AS Centro, adultos.Nombre, adultos.Apellido FROM centros INNER JOIN adultos ON centros.nombre = adultos.centro WHERE centros.nombre = "'+center+'" ORDER BY adultos.Apellido;'
            mycursor.execute(query)
            resultados = mycursor.fetchall()
            if resultados == 0:
                print('No se encontraron resultados con el nombre del centro especificado.')
            else:
                for registro in resultados:
                    print('Centro: ',registro[0], ' ¬Nombre:', registro[1], '¬Apellido: ', registro[2] )
                mycursor.close()
        except Exception as miError:
                print('Fallo Ejecutando el Procedimiento')
                print(miError)
            
    def verAlgo2 (self):
         try:
             
             mycursor=self.miConexion.cursor()
             query = 'SELECT categorias.nombre, actividades.nombre, actividades.fecha, actividades.Descripcion, centros.Direccion FROM (categorias INNER JOIN actividades ON categorias.idCategoria = actividades.iDCategoria) INNER JOIN centros ON centros.nombre = actividades.Centro WHERE actividades.fecha >= CURDATE() ORDER BY actividades.fecha;'
             mycursor.execute(query)
             resultados = mycursor.fetchall()
             if resultados == 0:
                 print('No se encontraron actividades futuras.')
             else:
                 for registro in resultados:
                     print('Categoria: ',registro[0], ' ¬Fecha:', registro[2], '¬Nombre: ', registro[1], '¬Decripcion: ' , registro[3], '¬Direccion: ', registro[4])
                 mycursor.close()
         except Exception as miError:
                 print('Fallo Ejecutando el Procedimiento')
                 print(miError)
             
    def verAlgo3 (self):
             try:
                 activity = input('Que actividad desea ver?')
                 mycursor=self.miConexion.cursor()
                 query = 'SELECT actividades.nombre, adultos.nombre, inscripcion.Calificacion FROM (adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto) INNER JOIN actividades ON actividades.idActividad = inscripcion.idActividad WHERE actividades.idActividad = "'+activity+'" ORDER BY inscripcion.Calificacion DESC;'
                 mycursor.execute(query)
                 resultados = mycursor.fetchall()
                 if resultados == 0:
                     print('No se encontraron actividades futuras.')
                 else:
                     for registro in resultados:
                         print('Actividad: ',registro[0], ' ¬Adulto:', registro[1], '¬Calificacion: ', registro[2])
                     mycursor.close()
             except Exception as miError:
                     print('Fallo Ejecutando el Procedimiento')
                     print(miError)
                 
    def verAlgo4(self):
            try:
                activity = input('Qué actividad desea ver? ')
                mycursor = self.miConexion.cursor()
                query = "SELECT adultos.Nombre, adultos.Apellido FROM adultos INNER JOIN inscripcion ON adultos.idAdulto = inscripcion.idAdulto INNER JOIN actividades ON actividades.idActividad = inscripcion.idActividad WHERE actividades.idActividad = '" + activity + "';"
                mycursor.execute(query)
                resultados = mycursor.fetchall()
        
                if resultados == 0:
                    print('No se encontraron adultos inscritos en la actividad especificada.')
                else:
                    print('Listado de adultos inscritos en la actividad:')
                    for registro in resultados:
                        print('Nombre:', registro[0], 'Apellido:', registro[1])
        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento.')
                print(miError)
                 
    def verAlgo5(self):
        try:
            idAdulto = input('Ingrese el ID del adulto: ')
            mycursor = self.miConexion.cursor()
            query = "SELECT actividades.Fecha, actividades.Nombre AS Actividad, inscripcion.Calificacion FROM actividades INNER JOIN inscripcion ON actividades.idActividad = inscripcion.IdActividad WHERE inscripcion.IdAdulto = '" + idAdulto + "';"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
    
            if resultados == 0:
                print('No se encontraron actividades realizadas por el adulto especificado.')
            else:
                print('Listado de actividades realizadas por el adulto:')
                for registro in resultados:
                    print('Fecha:', registro[0], 'Actividad:', registro[1], 'Calificación:', registro[2])
    
            mycursor.close()
        except Exception as miError:
            print('Fallo ejecutando el procedimiento.')
            print(miError)
            
    def verAlgo6(self):
        try:
            centro = input('Ingrese el nombre del centro: ')
            mycursor = self.miConexion.cursor()
            query = "SELECT actividades.Fecha, actividades.Nombre AS Actividad, inscripcion.Calificacion FROM actividades INNER JOIN inscripcion ON actividades.idActividad = inscripcion.IdActividad WHERE actividades.Centro = '" + centro + "' ORDER BY actividades.Fecha;"
            mycursor.execute(query)
            resultados = mycursor.fetchall()
    
            if resultados == 0:
                print('No se encontraron actividades realizadas en el centro especificado.')
            else:
                print('Listado de actividades realizadas en el centro:')
                for registro in resultados:
                    print('Fecha:', registro[0], 'Actividad:', registro[1], 'Calificación:', registro[2])
    
            mycursor.close()
        except Exception as miError:
            print('Fallo ejecutando el procedimiento.')
            print(miError)