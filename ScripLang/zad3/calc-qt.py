from PyQt5 import QtWidgets, QtGui, QtCore
from sys import argv
from Calculator import Calculator

class CalculatorViewer( QtWidgets.QDialog ):

    def __init__( self):
        super().__init__( flags = QtCore.Qt.Window )
        self.setWindowTitle( "Sumkowy Kalkulator" )
        self.__index = 0
        self.__calculator = Calculator()
        self.__equatation_label = QtWidgets.QLabel(self.__calculator.Display)
        self.__buttonMatrix = self.createButtons()
        b1 = QtWidgets.QVBoxLayout()
        b1.addWidget(self.__equatation_label, QtCore.Qt.AlignRight)
        buttonLayout = QtWidgets.QGridLayout()

        row_idx = 0;
        for button_row in self.__buttonMatrix:
            col_idx = 0
            for [button, rowspan, colspan] in button_row:
                buttonLayout.addWidget(button, row_idx, col_idx, rowspan, colspan)
                col_idx += 1
            row_idx += 1
        b1.addLayout(buttonLayout)
        self.setLayout(b1)

    # Domyślny rozmiar okna.
    def sizeHint( self ):
        return QtCore.QSize( 400, 300 )

    def createButtons(self):

        buttons = [

            [
                self.createButton("C/CE"),
                self.createButton("OFF"),
                self.createButton("\u221A"),
                self.createButton("\u0025")
            ],
            [
                self.createButton("MRC"),
                self.createButton("M-"),
                self.createButton("M+"),
                self.createButton("\u00F7")
            ],
            [
                self.createButton("7"),
                self.createButton("8"),
                self.createButton("9"),
                self.createButton("x")
            ],
            [
                self.createButton("4"),
                self.createButton("5"),
                self.createButton("6"),
                self.createButton("-")
            ],
            [
                self.createButton("1"),
                self.createButton("2"),
                self.createButton("3"),
                self.createButton("+", rowspan=2),
            ],
            [
                self.createButton("0"),
                self.createButton("."),
                self.createButton("="),
            ]
        ]
        return buttons

    def createButton(self,char, rowspan = 1, colspan=1):
        button = QtWidgets.QPushButton(char)
        button.clicked.connect(self.make_calluser(char))
        button.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding);
        return [button,rowspan,colspan]

    def make_calluser(self, name):
        if name == "\u00F7":
            name = "/"

        def calluser():
            self.__calculator.Press(name)
            self.__equatation_label.setText(self.__calculator.Display)
        return calluser


a = QtWidgets.QApplication( argv )
t = QtCore.QTranslator()
t.load( "qt_" + QtCore.QLocale.system().name(), QtCore.QLibraryInfo.location( QtCore.QLibraryInfo.TranslationsPath ) )
a.installTranslator( t )
w = CalculatorViewer()
w.show()
a.exec_()
