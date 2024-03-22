import sys
import socket
from PySide6.QtWidgets import (QApplication, QMainWindow, QStatusBar, QLineEdit, QSpinBox, QLabel, QVBoxLayout, QWidget,QDial, QPushButton, QMessageBox, QTextEdit)



class VentanaPrincipal(QMainWindow):


    def __init__(self):
        #llamada a constructor de la clase padre
        super().__init__()
        #widgets
        self.setWindowTitle("Monitor Vehículo")
        etiqueta=QLabel("Motor 1")
        campoTexto=QLineEdit('')
        self.spinBox = QSpinBox(value=0, maximum=255, minimum=0, prefix='', suffix='', singleStep=10)
        controlVelocidad=QDial()
        controlVelocidad.setRange(0,255)
        controlVelocidad.setSingleStep(1)
        botonEnviar=QPushButton("Enviar")
        botonEnviar.clicked.connect(self.enviarDatos)
        editTexto= QTextEdit()
        #layout
        layoutVertical=QVBoxLayout()
        #Asigancaion del layout
        layoutVertical.addWidget(etiqueta)
        layoutVertical.addWidget(campoTexto)
        layoutVertical.addWidget(self.spinBox)
        layoutVertical.addWidget(controlVelocidad)
        layoutVertical.addWidget(botonEnviar)
        layoutVertical.addWidget(editTexto)
        #No inventes
        widget = QWidget()
        widget.setLayout(layoutVertical)
        self.setCentralWidget(widget)
    def enviarDatos(self):
        dialogoEnviar=QMessageBox(self)
        dialogoEnviar.setWindowTitle("Monitor")
        dialogoEnviar.setText("Enviar Datos al Vehículo? ")
        dialogoEnviar.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        botonSeleccionado=dialogoEnviar.exec()
        if botonSeleccionado == QMessageBox.Yes:
            print(self.spinBox.value())
            self.enviaDatosSocket()
        else:
            print("Cancel")

    def enviaDatosSocket(self):
        direccionVehiculo='192.168.1.65'
        puertoVehiculo=2525
        MENSAJE="M1,V"+str(self.spinBox.value())+';'
        BUFFER_SIZE=1024
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
            socket_tcp.connect((direccionVehiculo, puertoVehiculo))
        # We convert str to bytes
            socket_tcp.send(MENSAJE.encode('utf-8'))
            data = socket_tcp.recv(BUFFER_SIZE)
            print(data)

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ventanaPrincipal = VentanaPrincipal()
    ventanaPrincipal.show()
    sys.exit(aplicacion.exec())



