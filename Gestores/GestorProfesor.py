from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

from vista.Opciones import Ui_MainWindow
from Gestores.Managers.TeacherManager import TeacherManager

class GestorProfesor(QMainWindow):
    def __init__(self):
        super(GestorProfesor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Btodos.clicked.connect(self.getAllProfesores)
        self.ui.Bnuevo.clicked.connect(self.newProfesor)
        self.ui.Bactualizar.clicked.connect(self.updateProfesor)
        self.ui.Beliminar.clicked.connect(self.deleteProfesor)
        self.ui.Bbuscar.clicked.connect(self.searchProfesor)
        self.ui.Bregresar.clicked.connect(self.closee)

    def getAllProfesores(self):
        self.tm = TeacherManager("all")
        self.tm.show()

    def newProfesor(self):
        self.tm = TeacherManager("new")
        self.tm.show()

    def updateProfesor(self):
        self.tm = TeacherManager("update")
        self.tm.show()

    def deleteProfesor(self):
        self.tm = TeacherManager("delete")
        self.tm.show()

    def searchProfesor(self):
        self.tm = TeacherManager("search")
        self.tm.show()

    def closee(self):
        self.close()