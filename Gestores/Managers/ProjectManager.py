from Conexion.Conection import Conection
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QInputDialog

from vista.Proyecto import Ui_MainWindow

class ProjectManager(QMainWindow):
    def __init__(self, modee):
        super(ProjectManager, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Bcrear.clicked.connect(self.newProyecto)
        self.ui.Bactualizar.clicked.connect(self.updateProyecto)
        self.ui.Beliminar.clicked.connect(self.deleteProyecto)
        self.ui.Bbuscar.clicked.connect(self.searchProyecto)
        self.ui.Bregresar.clicked.connect(self.closee)

        self.conection = Conection()
        self.mode = modee
        self.setup()
        self.modo()
        self.getAllProyectos()
    
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
            a = QInputDialog.getText(self, "Información", "Ingrese el id del departamento que desea modificar")
            self.searchProyecto(int(a[0]))
        elif self.mode == "delete":
            self.ui.Beliminar.setDisabled(False)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lpresupuesto.setDisabled(True)
            self.ui.dateEdit.setDisabled(True)
            self.ui.Clider.setDisabled(True)
        elif self.mode == "search":
            self.ui.Beliminar.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(False)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lpresupuesto.setDisabled(True)
            self.ui.dateEdit.setDisabled(True)
            self.ui.Clider.setDisabled(True)
        else:
            self.ui.Beliminar.setDisabled(True)
            self.ui.Bactualizar.setDisabled(True)
            self.ui.Bcrear.setDisabled(True)
            self.ui.Bbuscar.setDisabled(True)
            self.ui.Lnombre.setDisabled(True)
            self.ui.Lpresupuesto.setDisabled(True)
            self.ui.dateEdit.setDisabled(True)
            self.ui.Clider.setDisabled(True)
            self.ui.Sid.setDisabled(True)
    
    def setup(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProfesores")
            self.jefes = []
            for result in cur.stored_results():
                for(id,nombre,dir,tel,pro) in result:
                    self.jefes.append(str(id)+"-"+nombre)
                    self.ui.Clider.addItem(str(id) + "-" + nombre)
            self.conection.desconection()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def setupNew(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.execute("SELECT MAX(idProyectos) FROM proyectos")
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
    
    def getAllProyectos(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("allProyectos")

            a = self.ui.tabla.rowCount()
            for i in range(a):
                self.ui.tabla.removeRow(0)
            fila = 0

            for result in cur.stored_results():
                for(id,nombre,presupuesto,fecha,lider) in result:
                    self.ui.tabla.insertRow(fila)
                    self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(id)))
                    self.ui.tabla.setItem(fila, 1, QTableWidgetItem(nombre))
                    self.ui.tabla.setItem(fila, 2, QTableWidgetItem(str(presupuesto)))
                    self.ui.tabla.setItem(fila, 3, QTableWidgetItem(str(fecha)))
                    self.ui.tabla.setItem(fila, 4, QTableWidgetItem(str(lider)))
                    fila = fila + 1
            self.conection.desconection()
            if fila == 0:
                QMessageBox.warning(self, "Error", "No hay proyectos")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
        
    def newProyecto(self):
        if self.ui.Lnombre.text() == "" or self.ui.Lpresupuesto.text() == "" or self.ui.dateEdit.text() == "":
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos")
        try:
            con = self.conection.conection()
            cur = con.cursor()
            f = self.ui.dateEdit.text()
            ff = f.split("/")[::-1]
            fecha = ff[0] + "-" + ff[1] + "-" + ff[2]
            cur.callproc("createProyecto", (self.ui.Sid.value(),self.ui.Lnombre.text(), int(self.ui.Lpresupuesto.text()), fecha, int(self.ui.Clider.currentText().split("-")[0])))
            con.commit()
            QMessageBox.information(self, "Información", "Proyecto creado")
            self.conection.desconection()
            self.getAllProyectos()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def updateProyecto(self):
        if self.ui.Lnombre.text() == "" or self.ui.Lpresupuesto.text() == "" or self.ui.dateEdit.text() == "":
            QMessageBox.warning(self, "Error", "Debe llenar todos los campos")
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("updateProyecto", (self.ui.Sid.value(),self.ui.Sid.value(),self.ui.Lnombre.text(), int(self.ui.Lpresupuesto.text()), self.ui.dateEdit.text(), int(self.ui.Clider.currentText().split("-")[0])))
            con.commit()
            QMessageBox.information(self, "Información", "Proyecto creado")
            self.conection.desconection()
            self.getAllProyectos()
            
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def deleteProyecto(self):
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("deleteProyecto", [self.ui.Sid.value()])
            con.commit()
            QMessageBox.information(self, "Información", "Proyecto eliminado")
            self.conection.desconection()
            self.getAllProyectos()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    
    def searchProyecto(self, id = None):
        if id is False:
            id = self.ui.Sid.value()
        try:
            con = self.conection.conection()
            cur = con.cursor()
            cur.callproc("getProyecto", [id])
            for result in cur.stored_results():
                for(id,nombre,presupuesto,fecha,lider) in result:
                    self.ui.Sid.setValue(int(id))
                    self.ui.Lnombre.setText(nombre)
                    self.ui.Lpresupuesto.setText(str(presupuesto))
                    self.ui.dateEdit.setDate(fecha)
                    if lider is None:
                        self.ui.Clider.setCurrentIndex(0)
                    else:
                        for i in self.jefes:
                            if i.split("-")[0] == str(lider):
                                self.ui.Clider.setCurrentText(i)
            self.conection.desconection()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
    


