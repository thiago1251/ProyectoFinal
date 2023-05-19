from Conex.Conexion import Conexion
from Modelo.Adulto import Adulto
from datetime import datetime

class AdmonAdultos:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonAdultos creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   ADULTOS')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Adulto')
            print('3. Agregar Adulto')
            print('4. Modificar Adulto')
            print('5. Eliminar Adulto')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Adultos")
            elif opcion == 1:
                self.verTodos()
            elif opcion == 2:
                self.buscarAdulto()
            elif opcion == 3:
                self.agregaAdulto()
            elif opcion == 4:
                self.modifyAdulto()
            elif opcion == 5:
                self.eliminaAdulto()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodos(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allAdultos')
            for result in mycursor.stored_results():
                for (IdAdulto, nombre, apellido, FechaDeNacimiento,Peso,Altura,ContactoEmergencia,Centro) in result:
                    elAdulto = Adulto(IdAdulto, nombre, apellido, FechaDeNacimiento,Peso,Altura,ContactoEmergencia,Centro)
         
                    print(elAdulto.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay adultos registrados")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarAdulto(self):
        idAdultoSearch = int(input('Digite el código del Adulto: '))
        if self.existeIdAdulto(idAdultoSearch) == False :
            print ("El Adulto no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getAdulto',[idAdultoSearch])
                for result in mycursor.stored_results():
                    for (IdAdulto, nombre, apellido, FechaDeNacimiento,Peso,Altura,ContactoEmergencia,Centro) in result:
                        elAdulto = Adulto(IdAdulto, nombre, apellido, FechaDeNacimiento,Peso,Altura,ContactoEmergencia,Centro)
                        print(elAdulto.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaAdulto(self):
        idAdultoNew = int(input('Digite el código del nuevo Adulto: '))
        if self.existeIdAdulto(idAdultoNew) == True :
            print ("El Adulto ya existe no se puede repetir")
        else:
                nombreNew = input('Digite el nombre del Adulto: ')
                apellidoNew = input('Digite el apellido del Adulto: ')
                fechaDeNacimientoNew = datetime.strptime(input('Diga la fecha de La Actividad (YYYY-MM-DD): '), '%Y-%m-%d')
                pesoNew = int(input('Digite el peso del Adulto'))
                alturaNew = int(input('Digite la Altura del Adulto'))
                contactoEmergenciaNew = input('Digite el telefono de Emergencia')
                centroNew = input('Digite el nombre del Centro al que pertenece el Adulto')
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newAdulto', [idAdultoNew, nombreNew, apellidoNew, fechaDeNacimientoNew, pesoNew, alturaNew, contactoEmergenciaNew, centroNew])
                    self.miConexion.commit()
                    print('El Adulto ha sido añadido...!!')
                    mycursor.close()
                except Exception as miError:
                    print('Fallo  ejecutando el procedimiento')
                    print(miError)

         

    def eliminaAdulto(self):

        idAdultoDel = int(input('Digite el código del Adulto a eliminar: '))
        if self.existeIdAdulto(idAdultoDel) == False :
            print ("El Adulto no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delAdulto', [idAdultoDel])
                self.miConexion.commit()
                print('El Adulto ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyAdulto(self):

        idAdultoOld = int(input('Digite código actual: '))
        if self.existeIdAdulto(idAdultoOld) == False :
            print ("El Adulto no existe")
        else :
            idAdultoNew = int(input('Digite nuevo código del Adulto: '))
            if idAdultoNew != idAdultoOld and self.existeIdAdulto(idAdultoNew) == True:
                print("Ya existe un Adulto con ese ID, No se puede modificar")
                
            else:
                      nombreNew = input('Digite el nombre del Adulto: ')
                      apellidoNew = input('Digite el apellido del Adulto: ')
                      fechaDeNacimientoNew = datetime.strptime(input('Diga la fecha de La Actividad (YYYY-MM-DD): '), '%Y-%m-%d')
                      pesoNew = int(input('Digite el peso del Adulto'))
                      alturaNew = int(input('Digite la Altura del Adulto'))
                      contactoEmergenciaNew = input('Digite el telefono de Emergencia')
                      centroNew = input('Digite el nombre del Centro al que pertenece el Adulto')
                        
            try:
                            mycursor = self.miConexion.cursor()
                            mycursor.callproc('modAdulto', [idAdultoNew, nombreNew, apellidoNew, fechaDeNacimientoNew, pesoNew, alturaNew, contactoEmergenciaNew, centroNew, idAdultoOld])
                            self.miConexion.commit()
                            print('El Adulto ha sido modificado..!!')
                            mycursor.close()
            except Exception as miError:
                            print('Fallo ejecutando el procedimiento')
                            print(miError)

    def existeIdAdulto (self,idAdulto):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM ADULTOS WHERE idAdulto = %s ;'
            mycursor.execute(query,[idAdulto])
            resultados = mycursor.fetchall()
            
            for registro in resultados:
                if registro[0] == 1:
                    return True
                return False
            mycursor.close()
        except Exception as miError :
            print('Fallo ejecutando el procedimiento')
            print(miError)
            
  