from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.SourseManager import SourseManager

class GestorFuente(QMainWindow):
    def __init__(self):
        super(GestorFuente, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllFuentes)
        self.ui.Bnuevo.clicked.connect(self.newFuente)
        self.ui.Bactualizar.clicked.connect(self.updateFuente)
        self.ui.Beliminar.clicked.connect(self.deleteFuente)
        self.ui.Bbuscar.clicked.connect(self.searchFuente)
        self.ui.Bregresar.clicked.connect(self.closee)
        
        



    def getAllFuentes(self):
        self.sm = SourseManager("all")
        self.sm.show()        

    def newFuente(self):
        self.sm = SourseManager("new")
        self.sm.show()
    
    def updateFuente(self):
        self.sm = SourseManager("update")
        self.sm.show()
    
    def deleteFuente(self):
        self.sm = SourseManager("delete")
        self.sm.show()
    
    def searchFuente(self):
        self.sm = SourseManager("search")
        self.sm.show()
    
    def closee(self):
        self.close()

    
        