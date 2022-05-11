from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.FinantialManager import FinantialManager

class GestorFinanciacion(QMainWindow):
    def __init__(self):
        super(GestorFinanciacion, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllFinanciacion)
        self.ui.Bnuevo.clicked.connect(self.newFinanciacion)
        self.ui.Bactualizar.clicked.connect(self.updateFinanciacion)
        self.ui.Beliminar.clicked.connect(self.deleteFinanciacion)
        self.ui.Bbuscar.clicked.connect(self.searchFinanciacion)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllFinanciacion(self):
        self.tm = FinantialManager("all")
        self.tm.show()
    
    def newFinanciacion(self):
        self.tm = FinantialManager("new")
        self.tm.show()
    
    def updateFinanciacion(self):
        self.tm = FinantialManager("update")
        self.tm.show()
    
    def deleteFinanciacion(self):
        self.tm = FinantialManager("delete")
        self.tm.show()
    
    def searchFinanciacion(self):
        self.tm = FinantialManager("search")
        self.tm.show()
    
    def closee(self):
        self.close()