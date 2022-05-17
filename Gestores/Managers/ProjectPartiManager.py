from Conexion.Conection import Conection
from mysql.connector import Error, errorcode
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QInputDialog, QMainWindow,
                             QMessageBox, QTableWidgetItem)
from vista.ParticipacionProy import Ui_MainWindow


class ProjectPartiManager(QMainWindow):
    def __init__(self, modee):
        super(ProjectPartiManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.createPartiProy)
        self.ui.Bactualizar.clicked.connect(self.updatePartiProy)
        self.ui.Beliminar.clicked.connect(self.deletePartiProy)
        self.ui.Bbuscar.clicked.connect(self.searchPartiProy)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.setup()
        self.modo()
        self.getAllPartiProy()

    def closee(self):
        self.close()

    def modo(self):
        if self.mode == "new":
            self.ui.Bcrear.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
        elif self.mode == "update":
            self.ui.Bactualizar.setDisabled(False)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.a = QInputDialog.getText(
                self, "Información", "Ingrese el id del proyecto que desea modificar")
            self.b = QInputDialog.getText(
                self, "Información", "Ingrese el id la fuente que desea modificar")
            self.searchPartiProy(int(self.a[0]), int(self.b[0]))
        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
        elif self.mode == "search":
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
        else:
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.spinBox.setDisabled(True)
            self.ui.Cprofesor.setDisabled(True)
            self.ui.Cproyecto.setDisabled(True)

    def setup(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProyectos")
            self.proy = []
            for result in cur.stored_results():
                for (id, nom, pre, fe, li) in result:
                    self.proy.append(str(id)+"-"+nom)
                    self.ui.Cproyecto.addItem(str(id)+"-"+nom)
            cur.callproc("allProfesores")
            self.jefes = []
            for result in cur.stored_results():
                for(id, nombre, dir, tel, pro) in result:
                    self.jefes.append(str(id)+"-"+nombre)
                    self.ui.Cprofesor.addItem(str(id) + "-" + nombre)
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def getAllPartiProy(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getAllPartiProy")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for result in cur.stored_results():
                for (prof, proy, horas) in result:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(prof)))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(proy)))
                    self.ui.tabla.setItem(
                        fila, 2, QTableWidgetItem(str(horas)))
                    fila += 1
            con.close()
            if fila == 0:
                QMessageBox.information(
                    self, "Información", "No hay proyectos registrados")
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def createPartiProy(self):
        prof = self.ui.Cprofesor.currentText().split(
            "-")[0]
        proy = self.ui.Cproyecto.currentText().split(
            "-")[0]
        if self.ui.spinBox.value() == 0:
            QMessageBox.critical(self, "Error", "Debe ingresar las horas")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("getProyecto", [proy])
                for result in cur.stored_results():
                    for(id, nombre, presupuesto, fecha, lider) in result:
                        if lider is None:
                            self.ui.Clider.setCurrentIndex(0)
                        else:
                            if lider == prof:
                                QMessageBox.warning(
                                    self, "Error", f"El profesor {prof} ya es lider del proyecto {proy}!")
                                con.commit()
                                con.close()
                                return
                cur.callproc("createPartiProy", (prof, proy,
                             int(self.ui.spinBox.value())))
                con.commit()
                con.close()
                QMessageBox.information(
                    self, "Información", "Proyecto registrado")
                self.getAllPartiProy()
            except Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    QMessageBox.warning(
                        self, "Error", f"El profesor {prof} ya está en el proyecto {proy}!")
            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al conectar con la base de datos")

    def updatePartiProy(self):
        if self.ui.spinBox.value() == 0:
            QMessageBox.critical(self, "Error", "Debe ingresar las horas")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updatePartiProy", (self.ui.Cprofesor.currentText().split(
                    "-")[0], self.ui.Cproyecto.currentText().split("-")[0], int(self.ui.spinBox.value()), int(self.a[0]), int(self.b[0])))
                con.commit()
                con.close()
                QMessageBox.information(
                    self, "Información", "Proyecto actualizado")
                self.getAllPartiProy()
            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al conectar con la base de datos")

    def deletePartiProy(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deletePartiProy", (int(self.ui.Cprofesor.currentText().split(
                "-")[0]), int(self.ui.Cproyecto.currentText().split("-")[0])))
            con.commit()
            con.close()
            QMessageBox.information(self, "Información", "Proyecto eliminado")
            self.getAllPartiProy()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def searchPartiProy(self, prof=None, proy=None):
        if prof is False:
            prof = self.ui.Cprofesor.currentText().split("-")[0]
            proy = self.ui.Cproyecto.currentText().split("-")[0]
        existe = False
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("searchPartiProy", (prof, proy))
            for result in cur.stored_results():
                for (prof, proy, horas) in result:
                    existe = True
                    self.ui.spinBox.setValue(int(horas))
                    for i in self.proy:
                        if i.split("-")[0] == str(proy):
                            self.ui.Cproyecto.setCurrentText(i)
                    for j in self.jefes:
                        if j.split("-")[0] == str(prof):
                            self.ui.Cprofesor.setCurrentText(j)

            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")
        if not existe:
            QMessageBox.warning(
                self, "Error", f"la participación del profesor {prof} con el proyecto {proy} no existe!")
            QTimer.singleShot(0, self.closee)
