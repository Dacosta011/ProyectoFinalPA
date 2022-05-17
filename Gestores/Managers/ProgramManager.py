from genericpath import exists
from Conexion.Conection import Conection
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QInputDialog
from PyQt6.QtCore import QTimer
from vista.Programa import Ui_MainWindow


class ProgramManager(QMainWindow):
    def __init__(self, modee):
        super(ProgramManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.newPrograma)
        self.ui.Bactualizar.clicked.connect(self.updatePrograma)
        self.ui.Beliminar.clicked.connect(self.deletePrograma)
        self.ui.Bbuscar.clicked.connect(self.searchPrograma)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.mode = modee
        self.conection = Conection()
        self.setup()
        self.modee()
        self.getAllProgramas()

    def closee(self):
        self.close()

    def modee(self):
        if self.mode == "new":
            self.ui.Bcrear.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Sid.setDisabled(True)
            self.setupNew()
        elif self.mode == "update":
            self.ui.Bactualizar.setDisabled(False)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Sid.setDisabled(True)
            a = QInputDialog.getText(
                self, "Información", "Ingrese el id del departamento que desea modificar")
            self.searchPrograma(int(a[0]))
        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ltelefono.setDisabled(True)
            self.ui.Cdirector.setDisabled(True)
            self.ui.Cdepartamento.setDisabled(True)
        elif self.mode == "search":
            self.ui.Beliminar.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ltelefono.setDisabled(True)
            self.ui.Cdirector.setDisabled(True)
            self.ui.Cdepartamento.setDisabled(True)
        else:
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ltelefono.setDisabled(True)
            self.ui.Cdepartamento.setDisabled(True)
            self.ui.Sid.setDisabled(True)
            self.ui.Cdirector.setDisabled(True)

    def setup(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allDepartamentos")
            self.depa = []
            for result in cur.stored_results():
                for (id, nom, ext, jefe) in result:
                    self.depa.append(str(id)+"-"+nom)
                    self.ui.Cdepartamento.addItem(str(id)+"-"+nom)
            cur.callproc("allProfesores")
            self.prof = []
            for result in cur.stored_results():
                for (id, nom, dir, tel, pro) in result:
                    self.prof.append(str(id)+"-"+nom)
                    self.ui.Cdirector.addItem(str(id)+"-"+nom)
            con.close()
        except Exception as e:
            print(e)

    def setupNew(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.execute("SELECT MAX(idProgramas) FROM programas")
            id = cur.fetchone()[0]
            if id is None:
                id = 1
            else:
                id += 1
            self.ui.Sid.setValue(int(id))
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", "Error al obtener el id")

    def newPrograma(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ltelefono.text() == "":
            QMessageBox.critical(self, "Error", "Faltan datos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("insertPrograma", [self.ui.Sid.value(), self.ui.Lnombre.text(), self.ui.Ltelefono.text(
                ), self.ui.Cdirector.currentText().split("-")[0], self.ui.Cdepartamento.currentText().split("-")[0]])
                con.commit()
                con.close()
                QMessageBox.information(self, "Información", "Programa creado")
                self.getAllProgramas()
            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al crear el programa")

    def updatePrograma(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ltelefono.text() == "":
            QMessageBox.critical(self, "Error", "Faltan datos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updatePrograma", (self.ui.Sid.value(), self.ui.Sid.value(), self.ui.Lnombre.text(), self.ui.Ltelefono.text(
                ), self.ui.Cdirector.currentText().split("-")[0], self.ui.Cdepartamento.currentText().split("-")[0]))
                con.commit()
                con.close()
                QMessageBox.information(
                    self, "Información", "Programa actualizado")
                self.getAllProgramas()
            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al actualizar el programa")

    def deletePrograma(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deletePrograma", [self.ui.Sid.value()])
            con.commit()
            con.close()
            QMessageBox.information(self, "Información", "Programa eliminado")
            self.getAllProgramas()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al eliminar el programa")

    def searchPrograma(self, id=None):
        if id is False:
            id = self.ui.Sid.value()
        existe = False
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getPrograma", [id])
            for result in cur.stored_results():
                for (id, nom, tel, dir, dep) in result:
                    existe = True
                    self.ui.Sid.setValue(int(id))
                    self.ui.Lnombre.setText(nom)
                    self.ui.Ltelefono.setText(tel)
                    if dir is None:
                        self.ui.Cdirector.setCurrentIndex(0)
                    if dep is None:
                        self.ui.Cdepartamento.setCurrentIndex(0)
                    else:
                        for i in self.depa:
                            if i.split("-")[0] == str(dep):
                                self.ui.Cdepartamento.setCurrentText(i)
                        for i in self.prof:
                            if i.split("-")[0] == str(dir):
                                self.ui.Cdirector.setCurrentText(i)
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Error", "Error al buscar el programa")
        if not existe:
            QMessageBox.warning(
                self, "Error", f"el programa con id {id} no existe!")
            QTimer.singleShot(0, self.closee)

    def getAllProgramas(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProgramas")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for result in cur.stored_results():
                for (id, nom, tel, dir, dep) in result:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(id)))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(nom))
                    self.ui.tabla.setItem(fila, 2, QTableWidgetItem(tel))
                    self.ui.tabla.setItem(fila, 3, QTableWidgetItem(str(dir)))
                    self.ui.tabla.setItem(fila, 4, QTableWidgetItem(str(dep)))
                    fila += 1
            con.close()
            if fila == 0:
                QMessageBox.information(
                    self, "Información", "No hay programas")
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al obtener los programas")

    def closee(self):
        self.close()
