class PartiProy:
    def __init__(self, profesor, proyecto,horas):
        self.profesor=profesor
        self.proyecto=proyecto
        self.horas=horas
    
    #getters and setters
    def getProfesor(self):
        return self.profesor
    def setProfesor(self,profesor):
        self.profesor=profesor
    def getProyecto(self):
        return self.proyecto
    def setProyecto(self,proyecto):
        self.proyecto=proyecto
    def getHoras(self):
        return self.horas
    def setHoras(self,horas):
        self.horas=horas
    def __str__(self):
        return "Profesor: "+self.profesor+"\nProyecto: "+self.proyecto+"\nHoras: "+str(self.horas)
        