class Inscripcion:
    #Constructor
    def __init__ (self, idAdultoNew, idActividadNew, calificacionNew):
        #Atributos
        self.idAdulto = idAdultoNew
        self.idActividad = idActividadNew
        self.calificacion = calificacionNew
        
    #Analizadores
    def getidAdulto(self):
        return self.idAdulto
    
    def getidActividad(self):
        return self.idActividad
    
    def getCalificacion(self):
        return self.calificacion
    
    #Modificadores
    def setidAdulto(self, idAdultoNew):
        self.idAdulto = idAdultoNew
        
    def setidActividad(self, idActividadNew):
        self.idActividad = idActividadNew
        
    def setCalificacion(self,calificacionNew):
        self.calificacion = calificacionNew
        
    def toString(self):
        return("idAdulto = ",self.idAdulto," idActividad = ",self.idActividad," Calificacion = ", self.calificacion)
    