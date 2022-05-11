from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.ProgramManager import ProgramManager

class GestorPrograma(QMainWindow):
    def __init__(self):
        super(GestorPrograma, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllProgramas)
        self.ui.Bnuevo.clicked.connect(self.newPrograma)
        self.ui.Bactualizar.clicked.connect(self.updatePrograma)
        self.ui.Beliminar.clicked.connect(self.deletePrograma)
        self.ui.Bbuscar.clicked.connect(self.searchPrograma)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllProgramas(self):
        self.tm = ProgramManager("all")
        self.tm.show()

    def newPrograma(self):
        self.tm = ProgramManager("new")
        self.tm.show()
    
    def updatePrograma(self):
        self.tm = ProgramManager("update")
        self.tm.show()
    
    def deletePrograma(self):
        self.tm = ProgramManager("delete")
        self.tm.show()
    
    def searchPrograma(self):
        self.tm = ProgramManager("search")
        self.tm.show()
    
    def closee(self):
        self.close()