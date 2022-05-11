from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.ProjectPartiManager import ProjectPartiManager

class GestorPartiProy(QMainWindow):
    def __init__(self):
        super(GestorPartiProy, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllPartiProy)
        self.ui.Bnuevo.clicked.connect(self.newPartiProy)
        self.ui.Bactualizar.clicked.connect(self.updatePartiProy)
        self.ui.Beliminar.clicked.connect(self.deletePartiProy)
        self.ui.Bbuscar.clicked.connect(self.searchPartiProy)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllPartiProy(self):
        self.tm = ProjectPartiManager("all")
        self.tm.show()
    
    def newPartiProy(self):
        self.tm = ProjectPartiManager("new")
        self.tm.show()
    
    def updatePartiProy(self):
        self.tm = ProjectPartiManager("update")
        self.tm.show()
    
    def deletePartiProy(self):
        self.tm = ProjectPartiManager("delete")
        self.tm.show()
    
    def searchPartiProy(self):
        self.tm = ProjectPartiManager("search")
        self.tm.show()
    
    def closee(self):
        self.close()
        