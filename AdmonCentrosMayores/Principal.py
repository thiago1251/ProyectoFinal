import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from Admon.AdmonProfesores import AdmonProfesores
from Admon.AdmonFuentes import AdmonFuentes
from Diseno.DPrincipal import Ui_MainWindow

class Principal (QMainWindow):
    def __init__(self):
        super(Principal,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BFuente_2.clicked.connect(self.profesor)
        self.ui.BFuente.clicked.connect(self.fuente)
        self.ui.BTerminar.clicked.connect(self.terminar)

    def fuente(self):
        print("Se llama a Fuente")
        self.ventanaFuente = AdmonFuentes()
        self.ventanaFuente.show()

    def profesor(self):
        print("Se llama a Profesor")
        self.ventanaProfesor = AdmonProfesores()
        self.ventanaProfesor.show()

    def terminar(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventanaPrincipal = Principal()
    ventanaPrincipal.show()
    sys.exit(app.exec())