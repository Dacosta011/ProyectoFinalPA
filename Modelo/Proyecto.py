class Proyecto:
    def __init__(self,id, nombre, presupuesto, fechainicio, lider):
        self.id = id
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.fechainicio = fechainicio
        self.lider = lider
    
    #getters and setters
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    def getPresupuesto(self):
        return self.presupuesto
    def setPresupuesto(self, presupuesto):
        self.presupuesto = presupuesto
    def getFechainicio(self):
        return self.fechainicio
    def setFechainicio(self, fechainicio):
        self.fechainicio = fechainicio
    def getLider(self):
        return self.lider
    def setLider(self, lider):
        self.lider = lider
    def __str__(self):
        return "Id: " + self.id + "\nNombre: " + self.nombre + "\nPresupuesto: " + self.presupuesto + "\nFecha de inicio: " + self.fechainicio + "\nLider: " + self.lider