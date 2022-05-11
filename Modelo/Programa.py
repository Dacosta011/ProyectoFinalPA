class Programa:

    def __init__(self,id,nombre,telefono,director,depto):
        self.id=id
        self.nombre=nombre
        self.telefono=telefono
        self.director=director
        self.depto=depto
    #getters and setters
    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    def getTelefono(self):
        return self.telefono
    def setTelefono(self,telefono):
        self.telefono=telefono
    def getDirector(self):
        return self.director
    def setDirector(self,director):
        self.director=director
    def getDepto(self):
        return self.depto
    def setDepto(self,depto):
        self.depto=depto
    def __str__(self):
        return "Id: "+self.id+"\nNombre: "+self.nombre+"\nTelefono: "+self.telefono+"\nDirector: "+self.director+"\nDepto: "+self.depto