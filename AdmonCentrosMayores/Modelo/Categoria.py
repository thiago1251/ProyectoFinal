class Categoria:
    #constructor
    def __init__(self,idCategoriaNew, nombreNew):
        #analizadores
        self.idCategoria = idCategoriaNew
        self.nombre = nombreNew
        print("Objeto de tipo Categoria creado...")
        
    #analizadores
    def getidCategoria(self):
        return self.idCategoria
    
    def getNombre(self):
        return self.nombre
    
    #modificadores
    
    def setidCategoria(self, idCategoriaNew):
        self.idCategoria = idCategoriaNew
        
    def setNombre(self, nombreNew):
        self.nombre = nombreNew
        
    def toString (self):
        return(" idCategoria = ", self.idCategoria," Nombre = ", self.nombre)
    