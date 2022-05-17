from distutils import extension

from Conexion.Conection import Conection
from Modelo.Fuente import Fuente
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QInputDialog, QMainWindow,
                             QMessageBox, QTableWidgetItem)
from vista.Departamento import Ui_MainWindow


class DepartamentoManager(QMainWindow):
    def __init__(self, modee):
        super(DepartamentoManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.newDepartamento)
        self.ui.Bactualizar.clicked.connect(self.updateDepartamento)
        self.ui.Bbuscar.clicked.connect(self.searchDepartamento)
        self.ui.Beliminar.clicked.connect(self.deleteDepartamento)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.setup()
        self.modo()
        self.getallDepartamentos()

    def closee(self):
        self.close()

    def modo(self):
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
            self.searchDepartamento(int(a[0]))
        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lextension.setDisabled(True)
            self.ui.Cjefe.setDisabled(True)
        elif self.mode == "search":
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lextension.setDisabled(True)
            self.ui.Cjefe.setDisabled(True)
        else:
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lextension.setDisabled(True)
            self.ui.Cjefe.setDisabled(True)
            self.ui.Sid.setDisabled(True)

    def setupNew(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.execute("SELECT MAX(idDepartamentos) FROM departamentos")
            id = cur.fetchone()[0]
            if id is None:
                id = 1
            else:
                id = id + 1
            self.ui.Sid.setValue(int(id))
            self.conection.desconection()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            self.conection.desconection()

    def setup(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProfesores")
            self.jefes = []
            for result in cur.stored_results():
                for(id, nombre, dir, tel, pro) in result:
                    self.jefes.append(str(id)+"-"+nombre)
                    self.ui.Cjefe.addItem(str(id) + "-" + nombre)
            self.conection.desconection()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def searchDepartamento(self, id=None):
        existe = False
        if id == False:
            id = self.ui.Sid.value()
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getDepartamento", [id])
            for result in cur.stored_results():
                for(id, nombre, extension, jefe) in result:
                    existe = True
                    self.ui.Sid.setValue(int(id))
                    self.ui.Lnombre.setText(nombre)
                    self.ui.Lextension.setText(extension)
                    if jefe is None:
                        self.ui.Cjefe.setCurrentIndex(0)
                    else:
                        for i in self.jefes:
                            if i.split("-")[0] == str(jefe):
                                self.ui.Cjefe.setCurrentText(i)
            self.conection.desconection()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        if not existe:
            QMessageBox.warning(
                self, "Error", f"el departamento con id {id} no existe!")
            QTimer.singleShot(0, self.closee)

    def newDepartamento(self):
        if self.ui.Lnombre.text() == "" or self.ui.Lextension.text() == "":
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                jefe = self.ui.Cjefe.currentText().split("-")[0]
                cur.callproc("createDepartamento", [self.ui.Sid.value(
                ), self.ui.Lnombre.text(), self.ui.Lextension.text(), jefe])
                con.commit()
                QMessageBox.information(
                    self, "Información", "Departamento creado")
                self.conection.desconection()
                self.getallDepartamentos()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def updateDepartamento(self):
        if self.ui.Lnombre.text() == "" or self.ui.Lextension.text() == "":
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updateDepartamento", [self.ui.Sid.value(), self.ui.Lnombre.text(
                ), self.ui.Lextension.text(), self.ui.Cjefe.currentText().split("-")[0] , self.ui.Sid.value()])
                con.commit()
                QMessageBox.information(
                    self, "Información", "Departamento actualizado")
                self.conection.desconection()
                self.getallDepartamentos()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def deleteDepartamento(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deleteDepartamento", [self.ui.Sid.value()])
            con.commit()
            QMessageBox.information(
                self, "Información", "Departamento eliminado")
            self.conection.desconection()
            self.getallDepartamentos()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def getallDepartamentos(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allDepartamentos")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for result in cur.stored_results():
                for(id, nombre, extension, jefe) in result:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(id)))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(nombre))
                    self.ui.tabla.setItem(fila, 2, QTableWidgetItem(extension))
                    self.ui.tabla.setItem(fila, 3, QTableWidgetItem(str(jefe)))
                    fila = fila + 1
            self.conection.desconection()
            if fila == 0:
                QMessageBox.warning(
                    self, "Error", "No hay departamentos registrados")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
