class Actividad:
    #Constructor
    def __init__(self, idActividadNew, nombreNew, descripcionNew, fechaNew, idCategoriaNew, centroNew):
        #Atributos
        self. idActividad = idActividadNew
        self. nombre = nombreNew
        self. descripcion = descripcionNew
        self. fecha = fechaNew
        self. idCategoria = idCategoriaNew
        self. centro = centroNew
        print("Objeto tipo Actividad creado...")
        
    #Analizadores
    
    def getidActividad(self):
        return self.idActividad
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getFecha(self):
        return self.fecha
    
    def getidCategoria(self):
        return self.idCategoria
    
    def getCentro(self):
        return self.centro
    
    #Modificadores
    
    def setidActividad(self, idActividadNew):
        self.idActividad = idActividadNew
        
    def setNombre (self, nombreNew):
        self.nombre = nombreNew
        
    def setDescripcionn ( self, descripcionNew):
        self.descripcion = descripcionNew
        
    def setFecha (self, fechaNew):
        self.fecha = fechaNew
        
    def setidCategoria(self, idCategoriaNew):
        self.idCategoria = idCategoriaNew
        
    def setCentro (self, centroNew):
        self.centro = centroNew
        
    def toString(self):
        return("idActividad = ",self.idActividad," Nombre = ", self.nombre," Descripcion = ", self.descripcion, " Fecha = ", self.fecha," idCategoria = ", self.idCategoria," Centro = ", self.centro)