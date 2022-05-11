from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.ProjectManager import ProjectManager

class GestorProyectos(QMainWindow):
    def __init__(self):
        super(GestorProyectos, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllProyectos)
        self.ui.Bnuevo.clicked.connect(self.newProyecto)
        self.ui.Bactualizar.clicked.connect(self.updateProyecto)
        self.ui.Beliminar.clicked.connect(self.deleteProyecto)
        self.ui.Bbuscar.clicked.connect(self.searchProyecto)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllProyectos(self):
        self.tm = ProjectManager("all")
        self.tm.show()
    
    def newProyecto(self):
        self.tm = ProjectManager("new")
        self.tm.show()
    
    def updateProyecto(self):
        self.tm = ProjectManager("update")
        self.tm.show()
    
    def deleteProyecto(self):
        self.tm = ProjectManager("delete")
        self.tm.show()
    
    def searchProyecto(self):
        self.tm = ProjectManager("search")
        self.tm.show()
    
    def closee(self):
        self.close()