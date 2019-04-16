from PyQt5 import QtWidgets, QtGui, QtCore
from sys import argv
from Calculator import Calculator

class IconsDrawer(QtWidgets.QWidget):

    def __init__( self):
        super().__init__()
        self.__memory_visible = False
        self.__error_visible = False
        self.__minus_visible = False

    def paintEvent( self, event ):
        w, h = self.width(), self.height()
        middle = h/2

        penSize = self.width()*0.1

        if penSize > 5:
            penSize = 5

        p = QtGui.QPainter( self )
        p.setPen( QtGui.QPen(QtCore.Qt.black, penSize) )
        p.setBrush( QtGui.QBrush( QtGui.QColor( 0, 0, 0 ) ) )

        memory_h_mid = middle - middle / 2
        memory_w_mid = w / 2
        memory_w_lSlash = memory_w_mid / 2
        memory_w_rSlash = memory_w_mid + memory_w_mid / 2
        memory_h_Slash_start = memory_h_mid + memory_h_mid - 10
        memory_h_Slash_end = 10

        if self.__memory_visible:
            p.drawLine(memory_w_lSlash, memory_h_Slash_start, memory_w_lSlash, memory_h_Slash_end)
            p.drawLine(memory_w_lSlash, memory_h_Slash_end, memory_w_mid, memory_h_mid)
            p.drawLine(memory_w_mid, memory_h_mid, memory_w_rSlash, memory_h_Slash_end)
            p.drawLine(memory_w_rSlash, memory_h_Slash_start, memory_w_rSlash, memory_h_Slash_end)

        minus_h = middle
        minus_w_start = 5
        minus_w_end = w - 5

        if self.__minus_visible:
            p.drawLine(minus_w_start, minus_h, minus_w_end, minus_h)

        error_h_mid = middle + middle / 2
        error_w_mid = 5
        error_h_lShlash_start = middle + 10
        error_h_lShlash_end = h - 10
        error_longer_end = w - 5
        error_mid_end = w / 2

        if self.__error_visible:
            p.drawLine(error_w_mid, error_h_lShlash_start, error_w_mid, error_h_lShlash_end)
            p.drawLine(error_w_mid, error_h_lShlash_start, error_longer_end, error_h_lShlash_start)
            p.drawLine(error_w_mid, error_h_lShlash_end, error_longer_end, error_h_lShlash_end)
            p.drawLine(error_w_mid, error_h_mid, error_mid_end, error_h_mid)

    def setMinusVisible(self, bool):
        self.__minus_visible = bool
        self.repaint()

    def setErrorVisible(self, bool):
        self.__error_visible = bool
        self.repaint()

    def setMemoryVisible(self, bool):
        self.__memory_visible = bool
        self.repaint()


class OpisViewer(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(flags=QtCore.Qt.Window)
        self.setWindowTitle("Opis Sumkowy Kalkulator")
        self.__label = QtWidgets.QLabel("Aplikacja Sumkowy Kalkulator została stworzona na potrzeby przedmiotu \"Języki skryptowe i ich zastosowania\". Aplikacja umożliwia przeprowadzenie prostych operacji matematycznych. Interfejs graficzny wykonany w PyQt.")
        self.__label.setWordWrap(True)
        self.__label.setAlignment(QtCore.Qt.AlignJustify)
        self.__close_button = QtWidgets.QPushButton("zamknij")

        b1 = QtWidgets.QVBoxLayout()
        self.__img = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("CalculatorIcon.png")
        pixmap = pixmap.scaled(256, 100)
        self.__img.setPixmap(pixmap)
        self.__img.setAlignment(QtCore.Qt.AlignHCenter)
        b1.addWidget(self.__img)
        b1.addWidget(self.__label)
        b1.addWidget(self.__close_button)
        self.setLayout(b1)

class CalculatorViewer( QtWidgets.QDialog ):

    def __init__( self):
        super().__init__(flags=QtCore.Qt.Window)
        self.setWindowTitle("Sumkowy Kalkulator")
        self.__index = 0
        self.__calculator = Calculator()
        self.__equatation_label = QtWidgets.QLabel(self.__calculator.Display)
        self.__icons = IconsDrawer()
        self.__buttonMatrix = self.createButtons()

        fontSize = self.height()*0.1
        font = QtGui.QFont("Times", fontSize, QtGui.QFont.Bold)

        self.__equatation_label.setFont(font)

        iconwidth = 0.1
        self.__icons.setMaximumWidth(self.width()*iconwidth)
        self.__icons.setMinimumHeight(80)

        extractAction0 = QtWidgets.QAction("&Opis...", self)
        extractAction0.setShortcut("Ctrl+O")
        extractAction0.setStatusTip('Opis aplikacji')
        extractAction0.triggered.connect(self.showOpis)

        extractAction = QtWidgets.QAction("&Wyjscie", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Zamknij aplikacje')
        extractAction.triggered.connect(exit)

        b1 = QtWidgets.QVBoxLayout()
        mainMenu = QtWidgets.QMenuBar()
        fileMenu = mainMenu.addMenu('&Plik')
        fileMenu.addAction(extractAction0)
        fileMenu.addAction(extractAction)
        b1.setMenuBar(mainMenu)
        screen = QtWidgets.QHBoxLayout()
        lScreen = QtWidgets.QVBoxLayout()
        lScreen.addWidget(self.__icons)
        rScreen = QtWidgets.QVBoxLayout()
        rScreen.addWidget(self.__equatation_label, 1, QtCore.Qt.AlignRight)
        screen.addLayout(lScreen)
        screen.addLayout(rScreen)

        b1.addLayout(screen)
        buttonLayout = QtWidgets.QGridLayout()

        row_idx = 0;
        for button_row in self.__buttonMatrix:
            col_idx = 0
            for [button, rowspan, colspan] in button_row:
                buttonLayout.addWidget(button, row_idx, col_idx, rowspan, colspan)
                col_idx += colspan
            row_idx += 1
        b1.addLayout(buttonLayout)
        self.setLayout(b1)

    def showOpis(self):
        w = OpisViewer()
        w.exec_()

    def resizeEvent(self, QResizeEvent):
        iconwidth = 0.05
        self.__icons.setMaximumWidth(self.width() * iconwidth)

        fontSize = self.height()*0.1
        font = QtGui.QFont("Times", fontSize, QtGui.QFont.Bold)
        self.__equatation_label.setFont(font)

    def sizeHint( self ):
        return QtCore.QSize( 400, 300 )

    def createButtons(self):

        buttons = [

            [
                self.createButton("C/CE", colspan=2),
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
        elif name == "\u0025":
            name = "p"
        elif name == "\u221A":
            name = "sqrt"

        def calluser():
            self.__calculator.Press(name)
            self.__equatation_label.setText(self.__calculator.Display)
            self.__icons.setMinusVisible(self.__calculator.IsNegative)
            self.__icons.setErrorVisible(self.__calculator.Error)
            self.__icons.setMemoryVisible(self.__calculator.IsMemorized)
        return calluser


a = QtWidgets.QApplication( argv )
t = QtCore.QTranslator()
t.load( "qt_" + QtCore.QLocale.system().name(), QtCore.QLibraryInfo.location( QtCore.QLibraryInfo.TranslationsPath ) )
a.installTranslator( t )
w = CalculatorViewer()
w.show()
a.exec_()
