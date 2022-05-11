class Profesor:

    def __init__(self,id,nombre,direccion,telefono,programa):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.id=id
        self.programa=programa
    #getters and setters
    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getDireccion(self):
        return self.direccion
    def setDireccion(self,direccion):
        self.direccion=direccion
    def getTelefono(self):
        return self.telefono
    def setTelefono(self,telefono):
        self.telefono=telefono
    def getPrograma(self):
        return self.programa
    def setPrograma(self,programa):
        self.programa=programa
    def __str__(self):
        return "id: "+str(self.id)+" nombre: "+self.nombre+" direccion: "+self.direccion+" telefono: "+self.telefono+" programa: "+self.programa