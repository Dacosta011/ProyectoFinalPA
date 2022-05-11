from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.DepartmentManager import DepartamentoManager

class GestorDepartamento(QMainWindow):
    def __init__(self):
        super(GestorDepartamento, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllDepartamentos)
        self.ui.Bnuevo.clicked.connect(self.newDepartamento)
        self.ui.Bactualizar.clicked.connect(self.updateDepartamento)
        self.ui.Beliminar.clicked.connect(self.deleteDepartamento)
        self.ui.Bbuscar.clicked.connect(self.searchDepartamento)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllDepartamentos(self):
        self.sm = DepartamentoManager("all")
        self.sm.show()
    
    def newDepartamento(self):
        self.sm = DepartamentoManager("new")
        self.sm.show()

    def updateDepartamento(self):
        self.sm = DepartamentoManager("update")
        self.sm.show()
    
    def deleteDepartamento(self):
        self.sm = DepartamentoManager("delete")
        self.sm.show()
    
    def searchDepartamento(self):
        self.sm = DepartamentoManager("search")
        self.sm.show()

    def closee(self):
        self.close()
        

