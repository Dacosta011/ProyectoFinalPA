from genericpath import exists
from Conexion.Conection import Conection
from mysql.connector import Error, errorcode
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QInputDialog
from PyQt6.QtCore import QTimer
from vista.Financiacion import Ui_MainWindow


class FinantialManager(QMainWindow):
    def __init__(self, modee):
        super(FinantialManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.newFinanciacion)
        self.ui.Bactualizar.clicked.connect(self.updateFinanciacion)
        self.ui.Beliminar.clicked.connect(self.deleteFinanciacion)
        self.ui.Bbuscar.clicked.connect(self.searchFinanciacion)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.setup()
        self.modo()
        self.getAllFinanciacion()

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
            self.searchFinanciacion(int(self.a[0]), int(self.b[0]))
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
            self.ui.Cfuente.setDisabled(True)
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
            cur.callproc("allFuentes")
            self.fuent = []
            for result in cur.stored_results():
                for (id, nom, dir, tel) in result:
                    self.fuent.append(str(id)+"-"+nom)
                    self.ui.Cfuente.addItem(str(id)+"-"+nom)
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def getAllFinanciacion(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allFinanciaciones")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for result in cur.stored_results():
                for (proy, fue, monto) in result:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(proy)))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(fue)))
                    self.ui.tabla.setItem(
                        fila, 2, QTableWidgetItem(str(monto)))
                    fila += 1
            con.close()
            if fila == 0:
                QMessageBox.information(
                    self, "Información", "No hay financiaciones registradas")
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def newFinanciacion(self):
        if self.ui.spinBox.value() == 0:
            QMessageBox.critical(self, "Error", "Debe ingresar un monto")
        else:
            proy = self.ui.Cproyecto.currentText().split(
                "-")[0]
            fuente = self.ui.Cfuente.currentText().split("-")[0]
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("createFinanciacion", (int(proy), int(
                    fuente), int(self.ui.spinBox.value())))
                con.commit()
                con.close()
                QMessageBox.information(
                    self, "Información", "Financiación registrada")
                self.getAllFinanciacion()
            except Error as err:
                if err.errno == errorcode.ER_DUP_ENTRY:
                    QMessageBox.warning(
                        self, "Error", f"El proyecto {proy} ya tiene la fuente {fuente}!")
            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al conectar con la base de datos")

    def updateFinanciacion(self):
        if self.ui.spinBox.value() == 0:
            QMessageBox.critical(self, "Error", "Debe ingresar un monto")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updateFinanciacion", [int(self.ui.Cproyecto.currentText().split("-")[0]), int(
                    self.ui.Cfuente.currentText().split("-")[0]), int(self.ui.spinBox.value()), int(self.a), int(self.b)])
                con.commit()
                con.close()
                QMessageBox.information(
                    self, "Información", "Financiación actualizada")
                self.getAllFinanciacion()

            except Exception as e:
                print(e)
                QMessageBox.critical(
                    self, "Error", "Error al conectar con la base de datos")

    def deleteFinanciacion(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deleteFinanciacion", (int(self.ui.Cproyecto.currentText().split(
                "-")[0]), int(self.ui.Cfuente.currentText().split("-")[0])))
            con.commit()
            con.close()
            QMessageBox.information(
                self, "Información", "Financiación eliminada")
            self.getAllFinanciacion()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")

    def searchFinanciacion(self, proy=None, fuente=None):
        if proy == False:
            proy = self.ui.Cproyecto.currentText().split("-")[0]
            fuente = self.ui.Cfuente.currentText().split("-")[0]
        existe = False
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getFinanciacion", (int(proy), int(fuente)))
            for result in cur.stored_results():
                for (proy, fue, monto) in result:
                    existe = True
                    self.ui.spinBox.setValue(int(monto))
                    for i in self.proy:
                        if str(proy) == i.split("-")[0]:
                            self.ui.Cproyecto.setCurrentText(i)
                    for i in self.fuent:
                        if str(fue) == i.split("-")[0]:
                            self.ui.Cfuente.setCurrentText(i)
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error", "Error al conectar con la base de datos")
        if not existe:
            QMessageBox.warning(
                self, "Error", f"la financiacion con proyecto {proy} y fuente {fuente} no existe!")
            QTimer.singleShot(0, self.closee)
