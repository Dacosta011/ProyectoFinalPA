from Conexion.Conection import Conection
from Modelo.Fuente import Fuente
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (QApplication, QInputDialog, QMainWindow,
                             QMessageBox, QTableWidgetItem)
from vista.Profesores import Ui_MainWindow


class TeacherManager(QMainWindow):
    def __init__(self, modee):
        super(TeacherManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.newTeacher)
        self.ui.Bactualizar.clicked.connect(self.updateTeacher)
        self.ui.Bbuscar.clicked.connect(self.searchTeacher)
        self.ui.Beliminar.clicked.connect(self.deleteTeacher)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.setup()
        self.modo()
        self.getallTeachers()

    def closee (self):
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
            a = QInputDialog.getText(self, "Información", "Ingrese el id del profesor que desea modificar")
            self.searchTeacher(int(a[0]))
        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)
            self.ui.Cprorama.setDisabled(True)
        elif self.mode == "search":
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)
            self.ui.Cprorama.setDisabled(True)
        else:
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Beliminar.setDisabled(True)
            self.ui.Sid.setDisabled(False)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Ldir.setDisabled(True)
            self.ui.Ltel.setDisabled(True)
            self.ui.Cprorama.setDisabled(True)
    
    def setupNew(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.execute("SELECT MAX(idProfesor) FROM profesores")
            id = cur.fetchone()[0]
            if id == None:
                id = 1
            else:
                id = id + 1
            self.ui.Sid.setValue(int(id))
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Error al obtener el id")

    def setup(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProgramas")
            self.programas = []
            for results in cur.stored_results():
                for (id,nom,tel,dir,dep) in results:
                    self.programas.append(str(id)+"-"+nom)
                    self.ui.Cprorama.addItem(str(id)+"-"+nom)
            con.close()
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Error al obtener los programas")

    def getallTeachers(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProfesores")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila =0
            for results in cur.stored_results():
                for (id,nom,dir,tel,pro) in results:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila,0,QTableWidgetItem(str(id)))
                    self.ui.tabla.setItem(fila,1,QTableWidgetItem(nom))
                    self.ui.tabla.setItem(fila,2,QTableWidgetItem(dir))
                    self.ui.tabla.setItem(fila,3,QTableWidgetItem(tel))
                    self.ui.tabla.setItem(fila,4,QTableWidgetItem(str(pro)))
                    fila = fila + 1
            con.close()
            if fila == 0:
                QMessageBox.warning(self, "Error", "No hay profesores registrados")
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error", "Error al obtener los profesores")

    def newTeacher(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ldir.text() == "" or self.ui.Ltel.text() == "":
            QMessageBox.warning(self, "Error", "Faltan datos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("insertProfesor",(self.ui.Sid.value(),self.ui.Lnombre.text(),self.ui.Ldir.text(),self.ui.Ltel.text(),self.ui.Cprorama.currentText().split("-")[0]))
                con.commit()
                con.close()
                QMessageBox.information(self, "Información", "Profesor registrado")
                self.getallTeachers()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Error al registrar el profesor")

    def updateTeacher(self):
        if self.ui.Lnombre.text() == "" or self.ui.Ldir.text() == "" or self.ui.Ltel.text() == "":
            QMessageBox.warning(self, "Error", "Faltan datos")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("updateProfesor",(self.ui.Sid.value(),self.ui.Sid.value(),self.ui.Lnombre.text(),self.ui.Ldir.text(),self.ui.Ltel.text(),self.ui.Cprorama.currentText().split("-")[0]))
                con.commit()
                con.close()
                QMessageBox.information(self, "Información", "Profesor actualizado")
                self.getallTeachers()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Error al actualizar el profesor")

    def deleteTeacher(self):
        if self.ui.Sid.value() == 0:
            QMessageBox.warning(self, "Error", "Seleccione un profesor")
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("deleteProfesor",[self.ui.Sid.value()])
                con.commit()
                con.close()
                QMessageBox.information(self, "Información", "Profesor eliminado")
                self.getallTeachers()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Error al eliminar el profesor")
    
    def searchTeacher(self, id = None):
        existe=False
        if id == False:
            id = self.ui.Sid.value()
        else:
            try:
                con = self.conection.conection()
                cur = con.cursor()
                cur.callproc("getProfesor",[id])
                for results in cur.stored_results():
                    for (id,nom,dir,tel,pro) in results:
                        existe=True
                        self.ui.Sid.setValue(int(id))
                        self.ui.Lnombre.setText(nom)
                        self.ui.Ldir.setText(dir)
                        self.ui.Ltel.setText(tel)
                        if pro == None:
                            self.ui.Cprorama.setCurrentIndex(0)
                        else:
                            for i in self.programas:
                                if i.split("-")[0] == str(pro):
                                    self.ui.Cprorama.setCurrentText(i)
                con.close()
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Error al obtener el profesor")
            if not existe:
                QMessageBox.warning(
                self, "Error", f"el profesor con id {id} no existe!")
                QTimer.singleShot(0, self.closee)
            
    
    def closee(self):
        self.close()
