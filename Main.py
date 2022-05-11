import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Main import Ui_SistemaGestionFacultad
from Gestores.GestorFuente import GestorFuente
from Gestores.GestorDepartamento import GestorDepartamento
from Gestores.GestorProfesor import GestorProfesor
from Gestores.GestorPrograma import GestorPrograma
from Gestores.GestorProyectos import GestorProyectos
from Gestores.GestorFinanciacion import GestorFinanciacion
from Gestores.GestorPartiProy import GestorPartiProy

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_SistemaGestionFacultad()
        self.ui.setupUi(self)

        self.ui.Bpartiproy_2.clicked.connect(self.Salir)
        self.ui.Bfuentes.clicked.connect(self.Fuentes)
        self.ui.Bdepartamentos.clicked.connect(self.Departamentos)
        self.ui.Bprofesores.clicked.connect(self.Profesores)
        self.ui.Bprogramas.clicked.connect(self.Programas)
        self.ui.Bproyectos.clicked.connect(self.Proyectos)
        self.ui.Bfinanciacion.clicked.connect(self.Financiacion)
        self.ui.Bpartiproy.clicked.connect(self.ParticipacionProyectos)
    
    def Salir(self):
        self.close()
    
    def Fuentes(self):
        self.gestor = GestorFuente()
        self.gestor.show()
    
    def Departamentos(self):
        self.gestor = GestorDepartamento()
        self.gestor.show()
    
    def Profesores(self):
        self.gestor = GestorProfesor()
        self.gestor.show()
    
    def Programas(self):
        self.gestor = GestorPrograma()
        self.gestor.show()
    
    def Proyectos(self):
        self.gestor = GestorProyectos()
        self.gestor.show()
    
    def Financiacion(self):
        self.gestor = GestorFinanciacion()
        self.gestor.show()
    
    def ParticipacionProyectos(self):
        self.gestor = GestorPartiProy()
        self.gestor.show()




if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())