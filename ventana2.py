import math
import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton

from Cliente import ClienteD
from ventana3 import Ventana3
from ventana4 import Ventana4


class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

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
        self.imagenFondo = QPixmap('imagenes/fondo2.png')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Arial", 20))
        self.letrero1.setStyleSheet("color: white;")

        self.vertical.addWidget(self.letrero1)

        self.vertical.addStretch()

        #---creamos un scroll
        self.scrollArea = QScrollArea()

        #--le ponemos transparente el fondo al scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")

        #--hacemos que se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        #--creamos una ventana contenedora para cada celda
        self.contenedora = QWidget()

        #--creamos una layout de grid para poner una cuadricula de elementos
        self.cuadricula = QGridLayout(self.contenedora)

        #-metemos la ventana contenedora al scroll
        self.scrollArea.setWidget(self.contenedora)

        #-metemos en el layout principal el scroll
        self.vertical.addWidget(self.scrollArea)

        #---abrimos el archivo en modo lectura
        self.file = open('datos/cliente.txt', 'rb')

        #---creamos una lista vacia para guardar los usuarios
        self.usuarios = []

        #--se recorre el archivo linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            #obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            #-se para si ya no hay mas registros en el archivo
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
            #---metemos el objeto en la lista de usuario
            self.usuarios.append(u)

        #---Cerramos el archivo
        self.file.close()

        #---Se tiene la lista con todos los usuarios
        #--obtenemos el numero de usuarios registrados
        #--consultamos el tamaño de la lista
        self.numeroUsuario = len(self.usuarios)

        #---contador para controlar a los usuarios en la lista
        self.contador = 0

        #---definimos cantidad de elementos para controlar a mostar por fila con columnas
        self.elementosPorColumna = 3

        #---calculamos el numero de filas
        #---redondemos el entero superior + 1, dividimos por elementos de columna
        self.numeroFilas = math.ceil(self.numeroUsuario / self.elementosPorColumna) + 1

        #---controlamos todos los botones por una variable
        self.botones = QButtonGroup()

        #---definimos un controlador de los botones
        #---debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                #validamos que se esten ingresando la cantidad de usuarios correcta
                if self.contador < self.numeroUsuario:
                    #en cada celda de la cuadricual va una ventana
                    self.ventanaAux = QWidget()
                    self.ventanaAux.setFixedHeight(100)
                    self.ventanaAux.setFixedWidth(200)

                    #se crea un layout para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    #se crea boton para cada usuario mostrando su cedula
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)
                    self.botonAccion.setFixedWidth(150)
                    self.botonAccion.setStyleSheet("background-color: #40AEFA;"
                                                   "color: white;"
                                                   "padding: 10px;")
                    #---metemos el boton en el layout vertical para que se muestre
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    #---agregamos el boton al grupo con su cedula como id
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    #agregamos un espacio
                    self.verticalCuadricula.addStretch()

                    #a la ventana le asignamos el layout vertical
                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    #a la cuadricula le agregamos la ventana en la fila y columna actual
                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    #aumentamos el contador
                    self.contador += 1

        #establecemos el metodo para qe funcionen todos los botones
        self.botones.idClicked.connect(self.metodo_accionBotones)

        #-----BOTON FORMA TABULAR------
        self.botonTabular = QPushButton("Forma Tabular")
        self.botonTabular.setFixedWidth(100)
        self.botonTabular.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 40px")

        self.botonTabular.clicked.connect(self.metodo_botonTabular)

        self.vertical.addWidget(self.botonTabular)

        #-----BOTON VOLVER-----
        #--se hace boton para volver a la ventana anterior
        self.botonVolver = QPushButton("Volver")
        self.botonVolver.setFixedWidth(90)
        self.botonVolver.setStyleSheet("background-color: blue;"
                                       "color: white;"
                                       "padding: 10px;"
                                       "margin-top: 2px")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        self.vertical.addWidget(self.botonVolver)


        # ---SE COLOCA AL FINAL---
        self.fondo.setLayout(self.vertical)

    #---metodo para controlar las acciones de los botones
    def metodo_accionBotones(self, cedulaUsuario):
        #print(cedulaUsuario)
        self.hide()
        self.ventana4 = Ventana4(self, cedulaUsuario)
        self.ventana4.show()

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_botonTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()








if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2

    ventana2.show()

    sys.exit(app.exec_())




