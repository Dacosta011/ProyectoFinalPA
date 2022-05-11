class FinanPro:
    def __init__(self,proyecto,fuente,monto):
        self.proyecto=proyecto
        self.fuente=fuente
        self.monto=monto
    
    #getters and setters
    def getProyecto(self):
        return self.proyecto
    def setProyecto(self,proyecto):
        self.proyecto=proyecto
    def getFuente(self):
        return self.fuente
    def setFuente(self,fuente):
        self.fuente=fuente
    def getMonto(self):
        return self.monto
    def setMonto(self,monto):
        self.monto=monto
    def __str__(self):
        return "Proyecto: "+self.proyecto+"\nFuente: "+self.fuente+"\nMonto: "+str(self.monto)