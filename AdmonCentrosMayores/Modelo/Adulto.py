class Adulto:
    #constructor
    def __init__ (self, idAdultoNew, nombreNew, apellidoNew, fechaDeNacimientoNew, pesoNew, alturaNew, contactoEmergenciaNew, centroNew):
        #atributos
        self.idAdulto = idAdultoNew
        self.nombre = nombreNew
        self.apellido = apellidoNew
        self.fechaDeNacimiento = fechaDeNacimientoNew
        self.peso = pesoNew
        self.altura = alturaNew
        self.contactoEmergencia = contactoEmergenciaNew
        self.centro = centroNew
        
    #analizadores 

    def getidAdulto(self):
        return self.idAdulto
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getFechaDeNacimiento(self):
        return self.fechaDeNacimiento
    
    def getPeso(self):
        return self.peso
    
    def getAltura(self):
        return self.altura
    
    def getContactoEmergencia(self):
        return self.contactoEmergencia
    
    def getCentro(self):
        return self.centro
    
    #modificadores
    
    def setidAdulto(self,idAdultoNew):
        self.idAdulto = idAdultoNew
        
    def setNombre(self, nombreNew):
        self.nombre = nombreNew
        
    def setApellido(self, apellidoNew):
        self.apellido = apellidoNew
        
    def setFechaDeNacimiento(self, fechaDeNacimientoNew):
        self.fechaDeNacimiento = fechaDeNacimientoNew
        
    def setPeso(self, pesoNew):
        self.peso = pesoNew
        
    def setAltura(self, alturaNew):
        self.altura = alturaNew
        
    def setContactoEmergencia(self,contactoEmergenciaNew):
        self.contactoEmergencia = contactoEmergenciaNew
        
    def setCentro(self, centroNew):
        self.centro= centroNew
        
    def toString(self):
        return ("idAdulto = ",self.idAdulto," nombre = ",self.nombre," apellido = ",self.apellido," Fecha de nacimiento= ", self.fechaDeNacimiento," peso = ", self.peso," altura = ", self.altura," Contacto de emergencia = ", self.contactoEmergencia," Centro = ",self.centro)
    