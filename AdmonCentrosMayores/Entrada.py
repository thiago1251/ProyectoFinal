from Admon.AdmonActividades import AdmonActividades
from Admon.AdmonAdultos import AdmonAdultos
from Admon.AdmonCategorias import AdmonCategorias
from Admon.AdmonCentros import AdmonCentros
from Admon.AdmonInscripciones import AdmonInscripciones
from Consultas import Consultas
class Entrada:

    #Constuctor
    def __init__(self):
        print('Objeto tipo Entrada creado y listo para usarse..!!')
        self.menu()

    # métodos
    def menu(self):
        opcion = -1
        while opcion != 0:
            print('==================================')
            print('............OPCIONES..............')
            print('==================================')
            print('0. Salir')          
            print('1. ACTIVIDADES')
            print('2. ADULTOS')
            print('3. CATEGORIAS')
            print('4. CENTROS')
            print('5. INSCRIPCIONES')
            print('6. BUSQUEDAS ESPECIALIZADAS')
            opcion = int(input('Digite su opción:'))

            if opcion == 0:
                print("Adios ..!!")

            elif opcion == 1:
                AdmonActividades()
            elif opcion == 2:
                AdmonAdultos()
            elif opcion == 3:
                AdmonCategorias()
            elif opcion == 4:
                AdmonCentros()
            elif opcion == 5:
                AdmonInscripciones()
            elif opcion == 6 :
                Consultas()
                
              

            else:
                print('Esa opción NO existe..!!!')


Entrada()