class Departamento:

    def __init__(self, id, nombre, extension, jefe):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.jefe = jefe
    
    # getters and setters
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getExtension(self):
        return self.extension
    def setExtension(self, extension):
        self.extension = extension
    def getJefe(self):
        return self.jefe
    def setJefe(self, jefe):
        self.jefe = jefe
    def __str__(self):
        return "Id: " + self.id + "\nNombre: " + self.nombre + "\nExtension: " + self.extension + "\nJefe: " + self.jefe