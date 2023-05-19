from Conex.Conexion import Conexion
from Modelo.Actividad import Actividad
from datetime import datetime

class AdmonActividades:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonActividades creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   ACTIVIDADES')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Actividad')
            print('3. Agregar Actividad')
            print('4. Modificar Actividad')
            print('5. Eliminar Actividad')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Actividades")
            elif opcion == 1:
                self.verTodas()
            elif opcion == 2:
                self.buscarActividad()
            elif opcion == 3:
                self.agregaActividad()
            elif opcion == 4:
                self.modifyActividad()
            elif opcion == 5:
                self.eliminaActividad()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodas(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allActividades')
            for result in mycursor.stored_results():
                for (idActividad,nombre,descripcion,fecha,iDCategoria,centro) in result:
                    laActividad = Actividad(idActividad, nombre, descripcion, fecha,iDCategoria, centro)
         
                    print(laActividad.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay actividades registrados")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarActividad(self):
        idActividadSearch = int(input('Digite el código de la Actividad: '))
        if self.existeIdActividad(idActividadSearch) == False :
            print ("La Actividad no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getActividad',[idActividadSearch])
                for result in mycursor.stored_results():
                    for (idActividad, nombre, descripcion, fecha,iDCategoria, centro) in result:
                        laActividad = Actividad(idActividad, nombre, descripcion, fecha,iDCategoria, centro)
                        print(laActividad.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaActividad(self):
        idActividadNew = int(input('Digite el código de la nueva Actividad: '))
        if self.existeIdActividad(idActividadNew) == True :
            print ("La actividad ya existe no se puede repetir")
        else:
            nombreNew = input('Digite el nombre de la Actividad: ')
            if self.existeNombre(nombreNew) == True:
                print('La Actividad ya existe no se puede repetir')
            else :
                descripcionNew = input('Digite la Descripcion de la Actividad: ')
                fechaNew = datetime.strptime(input('Diga la fecha de La Actividad (YYYY-MM-DD): '), '%Y-%m-%d')
                idCategoriaNew = int(input('Digite la Categoria de la actividad '))
                centroNew = input('Digite el centro de la actividad ')
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newActividad', [idActividadNew, nombreNew, descripcionNew, fechaNew, idCategoriaNew, centroNew])
                    self.miConexion.commit()
                    print('La Actividad ha sido creada...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)

         

    def eliminaActividad(self):

        idActividadDel = int(input('Digite el código de la Actividad a eliminar: '))
        if self.existeIdActividad(idActividadDel) == False :
            print ("La Actividad no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delActividad', [idActividadDel])
                self.miConexion.commit()
                print('La actividad ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyActividad(self):

        idActividadOld = int(input('Digite código actual: '))
        if self.existeIdActividad(idActividadOld) == False :
            print ("La Actividad no existe")
        else :
            idActividadNew = int(input('Digite nuevo código de la Actividad: '))
            if idActividadNew != idActividadOld and self.existeIdActividad(idActividadNew) == True:
                print("Ya existe la Actividad con ese ID, No se puede modificar")
                
            else:
                    nombreNew = input('Digite el nuevo nombre de la Actividad: ')
                    if self.existeNombre(nombreNew) == True:
                        print('La Actividad ya existe no se puede repetir')
                    
                    else:
                        descripcionNew = input('Digite la Descripcion de la Actividad: ')
                        fechaNew = datetime.strptime(input('Diga la fecha de La Actividad (YYYY-MM-DD): '), '%Y-%m-%d')
                        idCategoriaNew = int(input('Digite la Categoria de la actividad '))
                        centroNew = input('Digite el centro de la actividad ')
                        
                        try:
                            mycursor = self.miConexion.cursor()
                            mycursor.callproc('modActividad', [idActividadNew, nombreNew, descripcionNew, fechaNew, idCategoriaNew, centroNew, idActividadOld])
                            self.miConexion.commit()
                            print('La Actividad ha sido modificada..!!')
                            mycursor.close()
                        except Exception as miError:
                            print('Fallo ejecutando el procedimiento')
                            print(miError)

    def existeIdActividad (self,idActividad):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM ACTIVIDADES WHERE idActividad = %s ;'
            mycursor.execute(query,[idActividad])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
            mycursor.close()
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
    def existeNombre (self,nombre):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM ACTIVIDADES WHERE nombre = %s ;'
            mycursor.execute(query,[nombre])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
            mycursor.close()
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
 