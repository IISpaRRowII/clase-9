import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication

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

        #---hacemos letrero
        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: white;")

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
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
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


    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())











