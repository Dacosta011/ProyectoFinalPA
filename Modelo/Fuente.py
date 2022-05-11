class Fuente:
    def __init__(self,id,nombre,direccion,telefono):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    # getters and setters
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getDireccion(self):
        return self.direccion
    def setDireccion(self, direccion):
        self.direccion = direccion
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono = telefono
    def __str__(self):
        return "Id: " + str(self.id) + "\nNombre: " + self.nombre + "\nDireccion: " + self.direccion + "\nTelefono: " + str(self.telefono)