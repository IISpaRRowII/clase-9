import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout

from Cliente import ClienteD


class Ventana4(QMainWindow):
    def __init__(self, anterior, cedula):
        super(Ventana4,self).__init__(None)

        self.ventanaAnterior = anterior
        self.cedulaUsuario = cedula

        self.setWindowTitle("Editar usuario")

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
        self.fondo.setStyleSheet("background-color: #7C8181")
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        #----- LAYOUT IZQUIERDO -----
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Editar Cliente")
        self.letrero1.setFont(QFont("Arial", 20))

        self.letrero1.setStyleSheet("background-color: white;"
                                    "color: black;")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Arial", 10))

        self.letrero2.setStyleSheet("color: white;"
                                    "background-color: #ABB5B5;"
                                    "margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid black;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)


        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)


        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        #--- BOTON EDITAR ---
        self.botonEditar = QPushButton("Editar")
        self.botonEditar.setFixedWidth(90)
        self.botonEditar.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 2px")

        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # --- BOTON LIMPIAR ---
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 2px")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonEditar,self.botonLimpiar)

        #--- BOTON ELIMINAR ---
        self.botonEliminar = QPushButton("Eliminar")
        self.botonEliminar.setFixedWidth(90)
        self.botonEliminar.setStyleSheet("background-color: blue;"
                                        "color: white;"
                                        "padding: 10px;"
                                        "margin-top: 2px")

        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        self.ladoIzquierdo.addRow(self.botonEliminar)

        #--- BOTON VOLVER ---
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 2px")

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        self.ladoIzquierdo.addRow(self.botonVolver)

        #-- Se agrega el layout izquierdo al layout horizontal --
        self.horizontal.addLayout(self.ladoIzquierdo)

        #----- LAYOUT DERECHO -----
        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText(" Editar Recuperar contraseña")
        self.letrero3.setFont(QFont("Arial", 20))
        self.letrero3.setStyleSheet("background-color: white;"
                                    "color: black;")

        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero4.setFont(QFont("Arial", 10))

        self.letrero4.setStyleSheet("color: white;"
                                    "background-color: #ABB5B5;"
                                    "margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid black;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoDerecho.addRow(self.letrero4)

        #--- ¿1?
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verifcación 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        #--- ¿2?
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        #--- ¿3?
        self.pregunta3 = QLineEdit()
        self.pregunta3.setStyleSheet("background-color: white;")
        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        #-- Agregamos al layout horizontal el layout derecho
        self.horizontal.addLayout(self.ladoDerecho)



        #--- PONER AL FINAL ---
        self.fondo.setLayout(self.horizontal)

        # --- VENTANA DE DIALOGO ---
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.ventanaDialogo.resize(400, 200)

        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()

        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: blue; color: white; padding: 10px;")

        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

        #-- Este metodo carga los datos del usuario en el formulario
        self.cargar_datos()


    def accion_botonEditar(self):

        self.datosCorrectos = True

        self.ventanaDialogo.setWindowTitle("Formulario de edición")

        if (
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Los password's no son iguales")

            self.ventanaDialogo.exec_()

        if (
            self.nombreCompleto.text() == ''
            or self.usuario.text() == ''
            or self.password.text() == ''
            or self.documento.text() == ''
            or self.correo.text() == ''
            or self.pregunta1.text() == ''
            or self.respuesta1.text() == ''
            or self.pregunta2.text() == ''
            or self.respuesta2.text() == ''
            or self.pregunta3.text() == ''
            or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debes seleccionar un usuario con documento valiado!")

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        if self.datosCorrectos:

            self.file = open('datos/cliente.txt', 'rb')

            usuarios = []

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
                usuarios.append(u)

                # ---Cerramos el archivo
            self.file.close()


            existeDocumento = False

            self.file = open('datos/cliente.txt', 'rb')

            usuarios = []

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
                usuarios.append(u)

            # ---Cerramos el archivo
            self.file.close()

            # -variable para controlar si existe el documento
            existeDocumento = False

            for u in usuarios:
                # comparamos el documento ingresado
                # si corresponde el documento, es el usuario correcto
                if int(u.documento) == self.cedulaUsuario:
                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()

                    existeDocumento = True

                    break

            if (
                    not existeDocumento
            ):
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                self.ventanaDialogo.exec_()

            self.file = open('datos/cliente.txt', 'wb')

            # recorremos la lista de usuarios
            # para guardar usuario por usuario en el archvio
            for u in usuarios:
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

                # si ya existe usuario con este documento
                # y si ya se edito correctamente
                if (
                        existeDocumento
                ):
                    self.mensaje.setText("Usuario actualizado correctamente!")

                    self.ventanaDialogo.exec_()

                    self.accion_botonVolver()

                self.file = open('datos/cliente.txt', 'rb')
                while self.file:
                    linea = self.file.readline().decode('UTF-8')
                    print(linea)
                    if linea == '':
                        break
                self.file.close()

    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonEliminar(self):

        self.datosCorrectos = True

        self.eliminar = False

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debe seleccionar un usuario con un documento valido!")

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        if self.datosCorrectos:

            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            self.ventanaDialogoEliminar.resize(400, 200)

            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            self.verticalEliminar = QVBoxLayout()

            self.mensajeEliminar = QLabel("¿Estas seguro de que deseas eliminar este registro de usuario?")

            self.mensajeEliminar.setStyleSheet("background-color: blue; color: white; padding: 10px;")

            self.verticalEliminar.addWidget(self.mensajeEliminar)

            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            self.verticalEliminar.addWidget(self.opcionesBox)

            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            self.file = open('datos/cliente.txt', 'rb')

            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                lista = linea.split(";")

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

                usuarios.append(u)

            self.file.close()

            existeDocumento = False

            for u in usuarios:
            # comparamos el documento ingresado
            # si corresponde el documento, es el usuario correcto
                if int(u.documento) == self.cedulaUsuario:
                    #eliminamos el usuario de la lista de usuarios
                    usuarios.remove(u)
                    existeDocumento = True
                    break

            #abrimos la lista en modo escritura escribiendo datos en binario
            self.file = open('datos/cliente.txt', 'wb')

            #recorremos la lista de usuarios
            #para guardar los usuarios restantes en el archivo
            for u in usuarios:
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

            if (
                    existeDocumento
            ):
                self.mensaje.setText("Usuario elminado exitosamente!")

                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()

    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):
        self.file = open('datos/cliente.txt', 'rb')

        usuarios = []

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
            usuarios.append(u)

        # ---Cerramos el archivo
        self.file.close()

        #-variable para controlar si existe el documento
        existeDocumento = False

        #buscamos en la lista usuario por usuario si existe la cedula
        #es la cedula seleccionada de la ventana anterior
        for u in usuarios:
            #comparamos el documento ingresado
            #si corresponde el documento, es el usuario correcto
            if int(u.documento) == self.cedulaUsuario:
                #mostranso los datos en el formulario
                self.nombreCompleto.setText(u.nombreCompleto)
                #hacemos que el nombre no se pueda editar
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                #hacemos que el documetno no se pueda editar
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)

                #indicamos que encontramos el documento
                existeDocumento = True
                #paramos el for
                break

        if (
            not existeDocumento
        ):
            self.mensaje.setText("NO existe usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            self.ventanaDialogo.exec_()

            self.accion_botonVolver()





if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana4 = Ventana4()

    ventana4.show()

    sys.exit(app.exec_())






