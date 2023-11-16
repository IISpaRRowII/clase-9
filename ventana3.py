import sys
import uuid

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication, QToolBar, QAction, QMessageBox

from Cliente import ClienteD


class Ventana3(QMainWindow):
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios Registrados")

        self.setWindowIcon(QtGui.QIcon("Imagenes/icono.png"))

        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/fondo3.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        #---abrimos el archivo en modo lectura
        self.file = open('datos/cliente.txt', 'rb')

        #--lista vacia para guardar los usuario
        self.usuarios = []

        #--recorremos el archivo, linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # -se para si ya no hay mas registros en el archivo
            if linea == '':
                break

            u = ClienteD(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )
            # ---metemos el objeto en la lista de usuario
            self.usuarios.append(u)

        # ---Cerramos el archivo
        self.file.close()

        # ---Se tiene la lista con todos los usuarios
        # --obtenemos el numero de usuarios registrados
        # --consultamos el tamaño de la lista
        self.numeroUsuario = len(self.usuarios)

        # ---contador para controlar a los usuarios en la lista
        self.contador = 0

        #establecemos la distribucion de los elementos en layout vertical
        self.vertical = QVBoxLayout()

        #---- CONSTRCUTOR DE MENU TOOLBAR ----
        self.toolBar = QToolBar('Main toolbar')
        self.toolBar.setIconSize(QSize(32, 32))
        self.addToolBar(self.toolBar)

        #--  delete --
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Delete',self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolBar.addAction(self.delete)

        #-- add --
        self.add = QAction(QIcon('imagenes/add.png'), '&Add',self)
        self.add.triggered.connect(self.accion_add)
        self.toolBar.addAction(self.add)

        #-- insert --
        self.insert = QAction(QIcon('imagenes/insert.png'), '&Insert',self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolBar.addAction(self.insert)

        #---- FIN DEL MENU TOOLBAR ----

        #---hacemos letrero
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: black;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        # ---creamos un scroll
        self.scrollArea = QScrollArea()


        # --hacemos que se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        #---creamos una tabla
        self.tabla = QTableWidget()

        #--definimos el nuemero de columnas que tendra la tabla
        self.tabla.setColumnCount(11)

        #-definimos el ancho de cada columna
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 150)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        #-definimos el texto de la cabecera
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        #-establecemos el numero de filas
        self.tabla.setRowCount(self.numeroUsuario)

        #---llenamos la tabla
        for u in self.usuarios:
            self.tabla.setItem(self.contador,0, QTableWidgetItem(u.nombreCompleto))
            #hacemos que el nombre no se pueda editar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            #hacemos que el document no se pueda editar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        #--metemos la tabla al scroll
        self.scrollArea.setWidget(self.tabla)

        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        #----BOTON VOLVER----
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 2px")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)

        #---- SIEMPRE SE AGREGA AL FINAL ----
        self.fondo.setLayout(self.vertical)

    def accion_delete(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self,'Warning', 'Para borrar, debe selecionar un registro')

        boton = QMessageBox.question(
            self,'Confirmation','¿Esta seguro de que quieres borrar este registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.No
        )

        if boton == QMessageBox.StandardButton.Yes:
            if (
                self.tabla.item(filaActual, 0).text() != '' and
                self.tabla.item(filaActual, 1).text() != '' and
                self.tabla.item(filaActual, 2).text() != '' and
                self.tabla.item(filaActual, 3).text() != '' and
                self.tabla.item(filaActual, 4).text() != '' and
                self.tabla.item(filaActual, 5).text() != '' and
                self.tabla.item(filaActual, 6).text() != '' and
                self.tabla.item(filaActual, 7).text() != '' and
                self.tabla.item(filaActual, 8).text() != '' and
                self.tabla.item(filaActual, 9).text() != '' and
                self.tabla.item(filaActual, 10).text() != ''
            ):

                #abirmos el archivo en modo lectura
                self.file = open('datos/cliente.txt', 'rb')

                #creamos una lista
                usuario = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos del string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # -se para si ya no hay mas registros en el archivo
                    if linea == '':
                        break

                    u = ClienteD(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8],
                        lista[9],
                        lista[10],
                    )
                    # ---metemos el objeto en la lista de usuario
                    usuario.append(u)

                    # ---Cerramos el archivo
                self.file.close()

                #recorremos la lista:
                for u in usuario:
                    #buscamos el usuario por documento
                    if (
                        u.documento == self.tabla.item(filaActual, 3).text()
                    ):

                        #removemos el usuario
                        usuario.remove(u)

                        break

                self.file = open('datos/cliente.txt', 'wb')

                for u in usuario:
                    self.file.write(bytes(u.nombreCompleto + ";"
                                          + u.usuario + ";"
                                          + u.password + ";"
                                          + u.documento + ";"
                                          + u.correo + ";"
                                          + u.pregunta1 + ";"
                                          + u.respuesta1 + ";"
                                          + u.pregunta2 + ";"
                                          + u.respuesta2 + ";"
                                          + u.pregunta3 + ";"
                                          + u.respuesta3, encoding='UTF-8'))

                self.file.close()

                #hacemos que se borre el registro de la tabla
                self.tabla.removeRow(filaActual)

                return QMessageBox.question(
                    self,'Confirmation','El registro ha sido eliminado exitosamente.',
                    QMessageBox.StandardButton.Yes
                )

            else:
                #hacemos que en la tabal no se vea el registro en caso de tratarse de una fila vacia
                self.tabla.removeRow(filaActual)

    def accion_add(self):

        #obtenemos el numero de filas que tiene la tabla
        ultimaFila = self.tabla.rowCount()

        #insertamos una fila nueva despues de la ultima fila
        self.tabla.insertRow(ultimaFila)

        #llenamos cada celda de la nueva fila con un string vacio
        self.tabla.setItem(ultimaFila, 0, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 1, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 2, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 3, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 4, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 5, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 6, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 7, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 8, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 9, QTableWidgetItem(''))
        self.tabla.setItem(ultimaFila, 10, QTableWidgetItem(''))

    def accion_insert(self):
        filaActual = self.tabla.currentRow()

        if filaActual < 0:
            return QMessageBox.warning(self, 'Warning','Para ingresar debe, seleccionar un registro')

        boton = QMessageBox.question(
            self, 'Confirmation','¿Esta segura de que quiere ingrear este nuevo registro?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        datosVacios = True

        if boton == QMessageBox.StandardButton.Yes:

            if (
                    self.tabla.item(filaActual, 0).text() != '' and
                    self.tabla.item(filaActual, 1).text() != '' and
                    self.tabla.item(filaActual, 2).text() != '' and
                    self.tabla.item(filaActual, 3).text() != '' and
                    self.tabla.item(filaActual, 4).text() != '' and
                    self.tabla.item(filaActual, 5).text() != '' and
                    self.tabla.item(filaActual, 6).text() != '' and
                    self.tabla.item(filaActual, 7).text() != '' and
                    self.tabla.item(filaActual, 8).text() != '' and
                    self.tabla.item(filaActual, 9).text() != '' and
                    self.tabla.item(filaActual, 10).text() != ''
            ):

                datosVacios = False

                # abirmos el archivo en modo lectura
                self.file = open('datos/cliente.txt', 'rb')

                # creamos una lista
                usuario = []

                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    # obtenemos del string una lista con 11 datos separados por ;
                    lista = linea.split(";")
                    # -se para si ya no hay mas registros en el archivo
                    if linea == '':
                        break

                    u = ClienteD(
                        lista[0],
                        lista[1],
                        lista[2],
                        lista[3],
                        lista[4],
                        lista[5],
                        lista[6],
                        lista[7],
                        lista[8],
                        lista[9],
                        lista[10],
                    )
                    # ---metemos el objeto en la lista de usuario
                    usuario.append(u)

                    # ---Cerramos el archivo
                self.file.close()

                existeRegistro = False

                existeDocumento = False

                for u in usuario:

                    if (
                            u.nombreCompleto == self.tabla.item(filaActual, 0).text() and
                            u.usuario == self.tabla.item(filaActual, 1).text() and
                            u.password == self.tabla.item(filaActual, 2).text() and
                            u.documento == self.tabla.item(filaActual, 3).text() and
                            u.correo == self.tabla.item(filaActual, 4).text() and
                            u.pregunta1 == self.tabla.item(filaActual, 5).text() and
                            u.respuesta1 == self.tabla.item(filaActual, 6).text() and
                            u.pregunta2 == self.tabla.item(filaActual, 7).text() and
                            u.respuesta2 == self.tabla.item(filaActual, 8).text() and
                            u.pregunta3 == self.tabla.item(filaActual, 9).text() and
                            u.respuesta3 == self.tabla.item(filaActual, 10).text()
                    ):

                        existeRegistro = True

                        return QMessageBox.warning(self, 'Warning', 'Registro duplicadp, no se puede registrar')

                        break

                if not existeRegistro:

                    for u in usuario:

                        if (
                            u.documento == self.tabla.item(filaActual, 3).text()
                        ):

                            existeDocumento = True

                            u.nombreCompleto = self.tabla.item(filaActual, 0).text()
                            u.usuario = self.tabla.item(filaActual, 1).text()
                            u.password = self.tabla.item(filaActual, 2).text()
                            u.documento = self.tabla.item(filaActual, 3).text()
                            u.correo = self.tabla.item(filaActual, 4).text()
                            u.pregunta1 = self.tabla.item(filaActual, 5).text()
                            u.respuesta1 = self.tabla.item(filaActual, 6).text()
                            u.pregunta2 = self.tabla.item(filaActual, 7).text()
                            u.respuesta2 = self.tabla.item(filaActual, 8).text()
                            u.pregunta3 = self.tabla.item(filaActual, 9).text()
                            u.respuesta3 = self.tabla.item(filaActual, 10).text()

                            self.file = open('datos/cliente.txt', 'wb')

                            for u in usuario:
                                self.file.write(bytes(u.nombreCompleto + ";"
                                                      + u.usuario + ";"
                                                      + u.password + ";"
                                                      + u.documento + ";"
                                                      + u.correo + ";"
                                                      + u.pregunta1 + ";"
                                                      + u.respuesta1 + ";"
                                                      + u.pregunta2 + ";"
                                                      + u.respuesta2 + ";"
                                                      + u.pregunta3 + ";"
                                                      + u.respuesta3, encoding='UTF-8'))

                            self.file.close()

                            return QMessageBox.question(
                                self, 'Confirmation', 'Los datos del registro se han editado exitosamente',
                                QMessageBox.StandardButton.Ok
                            )

                            #paramos el for
                            break

                    #si se trata de un usuario nuevo
                    if not existeDocumento:
                        #abrimos el archivo en mdo agregar escribiendo datos en binario
                        self.file = open('datos/cliente.txt', 'ab')

                        #agregamos los datos de la fila en el nuevo archivo
                        self.file.write(bytes(self.tabla.item(filaActual, 0).text() + ";"
                                              + self.tabla.item(filaActual, 1).text() + ";"
                                              + self.tabla.item(filaActual, 2).text() + ";"
                                              + self.tabla.item(filaActual, 3).text() + ";"
                                              + self.tabla.item(filaActual, 4).text() + ";"
                                              + self.tabla.item(filaActual, 5).text() + ";"
                                              + self.tabla.item(filaActual, 6).text() + ";"
                                              + self.tabla.item(filaActual, 7).text() + ";"
                                              + self.tabla.item(filaActual, 8).text() + ";"
                                              + self.tabla.item(filaActual, 9).text() + ";"
                                              + self.tabla.item(filaActual, 10).text() + "\n", encoding='UTF-8'))



                        self.file.seek(0, 2)
                        self.file.close()

                    return QMessageBox.question(
                        self, 'Confirmation', 'Los datos del registro se han ingreado correctamente',
                        QMessageBox.StandardButton.Ok
                    )

            if datosVacios:
                return QMessageBox.warning(self, 'Warning','Debe ingresar todos los datos en el registro')

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())











