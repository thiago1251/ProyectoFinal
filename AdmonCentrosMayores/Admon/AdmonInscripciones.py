from Conex.Conexion import Conexion
from Modelo.Inscripcion import Inscripcion


class AdmonInscripciones:

        def __init__(self):
            self.con = Conexion()
            self.miConexion = self.con.conectar()
            
            print('Objeto tipo AdmonInscripciones creado y listo para usarse..!!')
           
            self.menu()

        def menu(self):
    
            opcion = -1
            while opcion != 0:
                print('===============')
                print(' INSCRIPCIONES')
                print('===============')
                print('0. Regresar')            
                print('1. Ver todas')
                print('2. Buscar Inscripcion')
                print('3. Agregar Inscripcion')
                print('4. Modificar Inscripcion')
                print('5. Eliminar Inscripcion')

                opcion = int(input('Digite su opción:'))

                if opcion == 0:
                    self.con.desconectar()
                    print("Fin del menu de Inscripciones en Proyectos")
                elif opcion == 1:
                    self.verTodas()
                elif opcion == 2:
                    self.buscarInscripcion()
                elif opcion == 3:
                    self.agregaInscripcion()
                elif opcion == 4:
                    self.modifyInscripcion()
                elif opcion == 5:
                    self.eliminaInscripcion()
                else:
                    print('Esa opción NO existe..!!!')
                input ()
                
        def verTodas(self):
            cant = 0
            try: 
                mycursor = self.miConexion.cursor()
                mycursor.callproc('allInscripciones')
                for result in mycursor.stored_results():
                    for (idAdulto, idActividad, calificacion) in result:
                        laIncripcion = Inscripcion(idAdulto, idActividad, calificacion)
             
                        print(laIncripcion.toString())
                        cant = cant + 1
                if cant == 0 :
                        print ("No hay Inscripciones registradas")
                mycursor.close()   
            except Exception as miError:
                print('Fallo ejecutando el procedimiento..!!')
                print(miError)
                
        def buscarInscripcion(self):
            idSearchAdulto = int(input('Diga el codigo del Adulto'))
            idSearchActividad = int(input('Diga el codigo de la Actividad'))
            if self.existeCodigo(idSearchAdulto, idSearchActividad)== False:
                print('El codigo no existe!')
            else :
                
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('getInscripcion', [idSearchAdulto, idSearchActividad])
                    for result in mycursor.stored_results():
                        for ( idAdulto, idActividad, calificacion) in result:
                            laInscripcion = Inscripcion(idAdulto, idActividad, calificacion)
                            print(laInscripcion.toString())
                            
                    mycursor.close()
                except Exception as miError:
                    print('Fallo ejecutando el procedimiento')
                    print(miError)
                    
        def agregaInscripcion(self):
            idNewAdulto = int(input('Diga el codigo nuevo del Adulto'))
            idNewActividad = int(input('Diga el codigo nuevo de la Actividad'))
            
            if self.existeCodigo(idNewAdulto, idNewActividad) == True :
                print ("La Participacion de Proyecto ya existe no se puede repetir")
                
            else :
                calificacionNew = int(input('Digite la nueva Calificacion: '))
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newInscripcion', [idNewAdulto,idNewActividad,calificacionNew])
                    self.miConexion.commit()
                    print('La Inscripcion ha sido creada...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)
                    
        def eliminaInscripcion(self):
            idAdultoDel = int(input('Diga el codigo actual del Adulto'))
            idActividadDel = int(input('Diga el codigo actual de la Actividad'))
            if self.existeCodigo(idAdultoDel,idActividadDel) == False :
                print ("La inscripcion no existe, no se puede eliminar")
            else :
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('delInscripcion', [idAdultoDel,idActividadDel])
                    self.miConexion.commit()
                    print('La Inscripcion de Proyecto ha sido eliminada..!!')
                    mycursor.close()
                except Exception as miError : 
                    print('Fallo ejecutanto el procedimiento')
                    print(miError)
                


        def modifyInscripcion(self):

            idAdultoOld = int(input('Diga el codigo actual del Adulto'))
            idActividadOld = int(input('Diga el codigo actual de la Actividad'))
            if self.existeCodigo(idAdultoOld,idActividadOld) == False :
                print ("La Inscripcion no existe")
            else :
                idAdultoNew = int(input('Diga el codigo nuevo del Adulto'))
                idActividadNew = int(input('Diga el codigo nuevo de la Actividad'))
                if idAdultoNew != idAdultoOld and idActividadNew != idActividadOld and self.existeCodigo(idAdultoNew, idActividadNew) == True:
                    print("Ya existe una Inscripcion con ese ID, No se puede modificar")
                else:
                    calificacionNew = input('Digite la nueva calificacion: ')
                    
                    
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modInscripcion', [idAdultoNew, idActividadNew, calificacionNew, idAdultoOld,idActividadOld])
                        self.miConexion.commit()
                        print('La inscripcion ha sido modificada..!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo ejecutando el procedimiento')
                        print(miError)

                    
        def existeCodigo(self,idAdulto,idActividad):
            try:
                mycursor = self.miConexion.cursor()
                query = 'SELECT COUNT(*) FROM INSCRIPCION WHERE idAdulto = %s AND idActividad = %s'      
                mycursor.execute(query,[idAdulto,idActividad])
                resultados = mycursor.fetchall()
                
                for registro in resultados:
                    if registro[0] == 1:
                        return True
                    return False
                mycursor.close()
            except Exception as miError :
                print('Fallo ejecutando el procedimiento')
                print(miError)