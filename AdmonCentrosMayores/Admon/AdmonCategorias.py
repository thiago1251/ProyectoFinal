from Conex.Conexion import Conexion
from Modelo.Categoria import Categoria


class AdmonCategorias:

    def __init__(self):
        self.con = Conexion()
        self.miConexion = self.con.conectar()
        
        print('Objeto tipo AdmonCategoria creado y listo para usarse..!!')
       
        self.menu()

    def menu(self):
        opcion = -1
        while opcion != 0:
            print('===============')
            print('   CATEGORIAS')
            print('===============')
            print('0. Regresar')            
            print('1. Ver todas')
            print('2. Buscar Categoria')
            print('3. Agregar Categoria')
            print('4. Modificar Categoria')
            print('5. Eliminar Categoria')

            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                self.con.desconectar()
                print("Fin del menu de Administración de Categoria")
            elif opcion == 1:
                self.verTodas()
            elif opcion == 2:
                self.buscarCategoria()
            elif opcion == 3:
                self.agregaCategoria()
            elif opcion == 4:
                self.modifyCategoria()
            elif opcion == 5:
                self.eliminaCategoria()
            else:
                print('Esa opción NO existe..!!!')
            input ()

    def verTodas(self):
        cant = 0
        try: 
            mycursor = self.miConexion.cursor()
            mycursor.callproc('allCategorias')
            for result in mycursor.stored_results():
                for (idCategoria, nombre) in result:
                    laCategoria = Categoria(idCategoria, nombre)
         
                    print(laCategoria.toString())
                    cant = cant + 1
            if cant == 0 :
                    print ("No hay categorias registradas")
            mycursor.close()   
        except Exception as miError:
            print('Fallo ejecutando el procedimiento..!!')
            print(miError)

    def buscarCategoria(self):
        idCategoriaSearch = int(input('Digite el código de la Categoria: '))
        if self.existeIdCategoria(idCategoriaSearch) == False :
            print ("La Categoria no existe")
        else :
            
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getCategoria',[idCategoriaSearch])
                for result in mycursor.stored_results():
                    for (idCategoria, nombre) in result:
                        laCategoria = Categoria(idCategoria, nombre)
                        print(laCategoria.toString())
                        
                mycursor.close()
            except Exception as miError:
                print('Fallo ejecutando el procedimiento')
                print(miError)
            
         


    def agregaCategoria(self):
        idCategoriaNew = int(input('Digite el código de la nueva Categoria: '))
        if self.existeIdCategoria(idCategoriaNew) == True :
            print ("La Categoria ya existe no se puede repetir")
        else:
                nombreNew = input('Digite el nombre de la Categoria: ')
                if self.existeNombre(nombreNew) == True:
                    print('Ese nombre ya existe no se puede repetir')
                else:
                
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('newCategoria', [idCategoriaNew, nombreNew])
                        self.miConexion.commit()
                        print('La Categoria ha sido añadida...!!')
                        mycursor.close()
                    except Exception as miError:
                        print('Fallo  ejecutando el procedimiento')
                        print(miError)
         

    def eliminaCategoria(self):

        idCategoriaDel = int(input('Digite el código de la categoria a eliminar: '))
        if self.existeIdCategoria(idCategoriaDel) == False :
            print ("La Categoria no existe, no se puede eliminar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCategoria', [idCategoriaDel])
                self.miConexion.commit()
                print('La Categoria ha sido eliminada..!!')
                mycursor.close()
            except Exception as miError : 
                print('Fallo ejecutanto el procedimiento')
                print(miError)
            


    def modifyCategoria(self):

        idCategoriaOld = int(input('Digite código actual: '))
        if self.existeIdCategoria(idCategoriaOld) == False :
            print ("La Categoria no existe")
        else :
            idCategoriaNew = int(input('Digite nuevo código de la categoria: '))
            if idCategoriaNew != idCategoriaOld and self.existeIdCategoria(idCategoriaNew) == True:
                print("Ya existe una Categoria con ese ID, No se puede modificar")
                
            else:
                      nombreNew = input('Digite el nombre de la Categoria: ')
                      if self.existeNombre(nombreNew) == True:
                          print('Ese nombre ya existe no se puede repetir') 
                      else:
                          
                          try:
                                mycursor = self.miConexion.cursor()
                                mycursor.callproc('modCategoria', [idCategoriaNew, nombreNew,idCategoriaOld])
                                self.miConexion.commit()
                                print('La categoria ha sido modificada..!!')
                                mycursor.close()
                          except Exception as miError:
                                print('Fallo ejecutando el procedimiento')
                                print(miError)

    def existeIdCategoria (self,idCategoria):
        try:
            mycursor = self.miConexion.cursor()
            query = 'SELECT count(*) FROM CATEGORIAS WHERE idCategoria = %s ;'
            mycursor.execute(query,[idCategoria])
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
            query = 'SELECT count(*) FROM CATEGORIAS WHERE nombre = %s ;'
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
            
            
