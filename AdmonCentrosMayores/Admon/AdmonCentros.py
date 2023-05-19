from Conex.Conexion import Conexion
from Modelo.Centro import Centro


class AdmonCentros:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonCentro creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   CENTROS')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todos')
            print('2. Buscar Centro')
            print('3. Agregar Centro')
            print('4. Modificar Centro')
            print('5. Eliminar Centro')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Centro")
            elif opcion == 1:
                self.verTodos()
            elif opcion == 2:
                self.buscarCentro()
            elif opcion == 3:
                self.agregaCentro()
            elif opcion == 4:
                self.modifyCentro()
            elif opcion == 5:
                self.eliminaCentro()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodos(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allCentros')
            for result in mycursor.stored_results():
                for (nombre, direccion,telefono) in result:
                    elCentro = Centro(nombre,direccion,telefono)
         
                    print(elCentro.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay centros registrados")
            else:
                    if cant > 0 :
                        print('Hay ' ,cant, 'Centros registrados' )
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarCentro(self):
        nombreSearch = input('Digite el nombre del Centro: ')
        if self.existeNombre(nombreSearch) == False :
            print ("EL centro no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCentro',[nombreSearch])
                for result in mycursor.stored_results():
                    for (nombre,direccion, telefono,) in result:
                        elCentro = Centro(nombre,direccion, telefono)
                        print(elCentro.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaCentro(self):
        nombreNew = input('Digite el nombre del nuevo Centro: ')
        if self.existeNombre(nombreNew) == True :
            print ("El centro ya existe no se puede repetir")
        else:
                
                telefonoNew = input('Digite el telefono nuevo: ')
                if self.existeTelefono(telefonoNew) == True :
                    print ("El numero de telefono ya existe no se puede repetir")
                else:
                    direccionNew = input('Digite la direccion del Centro')
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('newCentro', [nombreNew,direccionNew, telefonoNew])
                        self.miConexion.commit()
                        print('El Centro ha sido añadido...!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo  ejecutando el procedimiento')
                        print(miError)
         

    def eliminaCentro(self):

        nombreDel = input('Digite el nombre del centro a eliminar: ')
        if self.existeNombre(nombreDel) == False :
            print ("El centro no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCentro', [nombreDel])
                self.miConexion.commit()
                print('El Centro ha sido eliminado..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyCentro(self):

        nombreOld = input('Digite nombre actual: ')
        if self.existeNombre(nombreOld) == False :
            print ("El centro no existe")
        else :
            nombreNew = input('Digite nuevo nombre del Centro: ')
            if nombreNew != nombreOld and self.existeNombre(nombreNew) == True:
                print("Ya existe un Centro con ese nombre, No se puede modificar")
                
            else:
                          telefonoNew = input('Digite el telefono nuevo: ')
                          if self.existeTelefono(telefonoNew) == True :
                              print ("El numero de telefono ya existe no se puede repetir")
                          else:
                              direccionNew = input('Digite la direccion del Centro')
                              try:
                                mycursor = self.miConexion.cursor()
                                mycursor.callproc('modCentro', [nombreNew,direccionNew,telefonoNew,nombreOld])
                                self.miConexion.commit()
                                print('El centro ha sido modificado..!!')
                                mycursor.close()
                              except Exception as miError:
                                print('Fallo ejecutando el procedimiento')
                                print(miError)


    
    def existeNombre (self,nombre):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM CENTROS WHERE nombre = %s ;'
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
    
    def existeTelefono (self,telefono):
       try:
           mycursor = self.miConexion.cursor()
           query = 'SELECT count(*) FROM CENTROS WHERE telefono = %s ;'
           mycursor.execute(query,[telefono])
           resultados = mycursor.fetchall()
           
           for registro in resultados:
               if registro[0] == 1:
                   return True
               return False
           mycursor.close()
       except Exception as miError :
           print('Fallo ejecutando el procedimiento')
           print(miError)

            



