class Centro:
    #Constructor
    
    def __init__(self, nombreNew,  direccionNew, telefonoNew):
        #Atributos
        self.nombre = nombreNew
        self.direccion = direccionNew
        self.telefono = telefonoNew
        print("Objeto de tipo Centro creado...")
        
    #Analizadores
    
    def getNombre(self):
        return self.nombre
            
    def getDireccion(self):
        return self.direccion
        
    def getTelefono(self):
        return self.telefono
    
   #Modificadores
    def setNombre(self, nombreNew):
        self.nombre = nombreNew
        
    def setDireccion(self, direccionNew):
        self.direccion = direccionNew
        
    def setTelefono(self, telefonoNew):
        self.telefono = telefonoNew
        
    def toString (self):
        return ("Nombre = ", self.nombre," Dirección = ", self.direccion," Telefono = ", self.telefono)
   
    
    
    
