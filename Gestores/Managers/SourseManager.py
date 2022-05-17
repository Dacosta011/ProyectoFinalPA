from Conexion.Conection import Conection
from Modelo.Fuente import Fuente
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QInputDialog, QMainWindow,
                             QMessageBox, QTableWidgetItem)
from vista.Fuentes import Ui_MainWindowFuente


class SourseManager(QMainWindow):
    def __init__(self, modee):
        super(SourseManager, self).__init__()
        self.ui = Ui_MainWindowFuente()
        self.ui.setupUi(self)

        self.ui.Bbuscar.clicked.connect(self.searchFuente)
        self.ui.Bactualizar.clicked.connect(self.updateFuente)
        self.ui.Bcrear.clicked.connect(self.newFuente)
        self.ui.Beliminar.clicked.connect(self.deleteFuente)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.modo()
        self.getAllFuentes()

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
            
            a = QInputDialog.getText(self, "Información", "Ingrese el id de la fuente que desea modificar")
            self.searchFuente(int(a[0]))

        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)
            
        elif self.mode == "search":
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)

        else:
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)
            self.ui.Sid.setDisabled(True)
    
    def getAllFuentes(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allFuentes")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for results in cur.stored_results():
                for (id,nombre, direccion, telefono) in results:
                    self.ui.tabla.insertRow(fila)
                    ccodigo =  QTableWidgetItem(str(id))
                    cnombre = QTableWidgetItem(str(nombre))
                    cdireccion = QTableWidgetItem(str(direccion))
                    ctelefono = QTableWidgetItem(str(telefono))

                    self.ui.tabla.setItem(fila, 0, ccodigo)
                    self.ui.tabla.setItem(fila, 1, cnombre)
                    self.ui.tabla.setItem(fila, 2, cdireccion)
                    self.ui.tabla.setItem(fila, 3, ctelefono)
                    fila += 1
            self.conection.desconection()
            if fila == 0:
                QMessageBox.information(self, "Información", "No hay fuentes registradas")
        except Exception as e:
            QMessageBox.information(self, "Información", "Error al obtener las fuentes")
            print(e)

    def setupNew(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.execute("select idFuente from fuentes where idFuente=(select max(idFuente) from fuentes)")
            for (id) in cur:
                self.ui.Sid.setValue(int(id[0] + 1))
            self.conection.desconection()
        except Exception as e:
            QMessageBox.information(self, "Información", "Error al obtener el id de la fuente")
            print(e)
    
    def searchFuente(self, id = None):
        if id == False:    
            id = self.ui.Sid.value()
        existe=False
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getFuentes", [int(id)])
            for results in cur.stored_results():
                for (id,nombre, direccion, telefono) in results:
                    existe=True
                    self.ui.Sid.setValue(int(id))
                    self.ui.Lnombre.setText(str(nombre))
                    self.ui.Ldir.setText(str(direccion))
                    self.ui.Ltel.setText(str(telefono))
            self.conection.desconection()
        except Exception as e:
            QMessageBox.information(self, "Información", "Error al obtener la fuente")
            print(e)
        if not existe:
            QMessageBox.warning(
                self, "Error", f"la fuente con id {id} no existe!")
            QTimer.singleShot(0, self.closee)
    
    def newFuente(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ldir.text() == "" or self.ui.Ltel.text() == "":
            QMessageBox.information(self, "Información", "Debe llenar todos los campos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("createFuente", (self.ui.Sid.value(), self.ui.Lnombre.text(), self.ui.Ldir.text(), self.ui.Ltel.text()))
                con.commit()
                QMessageBox.information(self, "Información", "Fuente creada")
                self.conection.desconection()
                self.getAllFuentes()
            
            except Exception as e:
                QMessageBox.information(self, "Información", "Error al crear la fuente")
                print(e)

    def updateFuente(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ldir.text() == "" or self.ui.Ltel.text() == "":
            QMessageBox.information(self, "Información", "Debe llenar todos los campos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updateFuente", (self.ui.Sid.value(), self.ui.Lnombre.text(), self.ui.Ldir.text(), self.ui.Ltel.text(), self.ui.Sid.value()))
                con.commit()
                QMessageBox.information(self, "Información", "Fuente actualizada")
                self.conection.desconection()
                self.getAllFuentes()
            except Exception as e:
                QMessageBox.information(self, "Información", "Error al actualizar la fuente")
                print(e)
        
    def deleteFuente(self):
        if self.ui.Sid.text() == "":
            QMessageBox.information(self, "Información", "Debe ingresar el id de la fuente")
            return
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deleteFuente", [self.ui.Sid.value()])
            con.commit()
            QMessageBox.information(self, "Información", "Fuente eliminada")
            self.conection.desconection()
            self.getAllFuentes()
        except Exception as e:
            QMessageBox.information(self, "Información", "Error al eliminar la fuente")
            print(e)

    def clear(self):
        self.ui.Sid.setValue(0)
        self.ui.Lnombre.setText("")
        self.ui.Ldir.setText("")
        self.ui.Ltel.setText("")

    def closee(self):
        self.close()
        
