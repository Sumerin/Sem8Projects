#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przeglądarka grafów, wersja z GUI w Qt.

from PyQt5 import QtWidgets, QtGui, QtCore
from graphs import Graph
from math import pi, sin, cos
from sys import argv


# Widget rysujący graf.
class GraphWidget( QtWidgets.QWidget ):

    # Inicjalizacja widgetu.
    def __init__( self, graph ):
        super().__init__()
        self.__graph = graph
        self.setSizePolicy( QtWidgets.QSizePolicy( QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding ) )
        self.setMinimumSize( 320, 200 )

    # Przerysowuje aktualnie pokazywany graf.
    def paintEvent( self, event ):
        w, h = self.width(), self.height()
        r = 0.45 * min( w, h )
        o = self.__graph.order()
        p = QtGui.QPainter( self )
        p.setPen( QtGui.QColor( 102, 154, 204 ) )
        p.setBrush( QtGui.QBrush( QtGui.QColor( 102, 154, 204 ) ) )
        for i,j in self.__graph.edges():
            xi = (w / 2) + cos( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            yi = (h / 2) + sin( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            xj = (w / 2) + cos( 2 * pi * (j / o) + 3 * pi / 2 ) * r
            yj = (h / 2) + sin( 2 * pi * (j / o) + 3 * pi / 2 ) * r
            p.drawLine( xi, yi, xj, yj )
        p.setPen( QtGui.QColor( 204, 128, 102 ) )
        p.setBrush( QtGui.QBrush( QtGui.QColor( 204, 128, 102 ) ) )
        for i in range( o ):
            x = (w / 2) + cos( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            y = (h / 2) + sin( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            p.drawPie( x - r / 25, y - r / 25, r / 12.5, r / 12.5, 0, 5760 )

    # Domyślny rozmiar widgetu.
    def sizeHint( self ):
        return QtCore.QSize( 320 + self.width(), 200 + self.height() )

    # Zmienia graf na podany.
    def setGraph( self, graph ):
        self.__graph = graph
        self.repaint()


# Główne okno przeglądarki grafów.
class GraphViewer( QtWidgets.QDialog ):

    # Tworzy wszystkie komponenty składające się na główne okno przeglądarki grafów.
    def __init__( self, graphs ):
        super().__init__( flags = QtCore.Qt.Window )
        self.setWindowTitle( "Przeglądarka grafów" )
        self.__graphs = graphs
        self.__index = 0
        self.__graph_label = QtWidgets.QLabel( "<b>" + self.__graphs[self.__index].g6() + "</b>" )
        self.__graph_view = GraphWidget( self.__graphs[self.__index] )
        self.__next_button = QtWidgets.QPushButton(
            QtWidgets.QApplication.instance().style().standardIcon( QtWidgets.QStyle.SP_ArrowRight ), ""
        )
        self.__previous_button = QtWidgets.QPushButton(
            QtWidgets.QApplication.instance().style().standardIcon( QtWidgets.QStyle.SP_ArrowLeft ), ""
        )
        self.__progress_label = QtWidgets.QLabel( "1 / " + str( len( self.__graphs ) ) )
        self.__previous_button.setEnabled( False )
        self.__previous_button.clicked.connect( self.__show_previous_graph )
        if len( self.__graphs ) == 1:
            self.__next_button.setEnabled( False )
        self.__next_button.clicked.connect( self.__show_next_graph )
        b1 = QtWidgets.QVBoxLayout()
        b1.addWidget( self.__graph_label, 0, QtCore.Qt.AlignCenter )
        b1.addWidget( self.__graph_view, 1, QtCore.Qt.AlignCenter )
        b2 = QtWidgets.QHBoxLayout()
        b2.addWidget( self.__previous_button )
        b2.addWidget( self.__progress_label, 1, QtCore.Qt.AlignCenter )
        b2.addWidget( self.__next_button )
        b1.addLayout( b2 )
        self.setLayout( b1 )

    # Domyślny rozmiar okna.
    def sizeHint( self ):
        return QtCore.QSize( 800, 600 )

    # Pokazuje następny graf.
    def __show_next_graph( self ):
        self.__index += 1
        self.__previous_button.setEnabled( True )
        if len( self.__graphs ) == self.__index + 1:
            self.__next_button.setEnabled( False )
        self.__graph_label.setText( "<b>" + self.__graphs[self.__index].g6() + "</b>" )
        self.__progress_label.setText( str( self.__index + 1 ) + " / " + str( len( self.__graphs ) ) )
        self.__graph_view.setGraph( self.__graphs[self.__index] )
        self.repaint()

    # Pokazuje poprzedni graf.
    def __show_previous_graph( self ):
        self.__index -= 1
        self.__next_button.setEnabled( True )
        if self.__index == 0:
            self.__previous_button.setEnabled( False )
        self.__graph_label.setText( "<b>" + self.__graphs[self.__index].g6() + "</b>" )
        self.__progress_label.setText( str( self.__index + 1 ) + " / " + str( len( self.__graphs ) ) )
        self.__graph_view.setGraph( self.__graphs[self.__index] )
        self.repaint()

# Główna część programu.
a = QtWidgets.QApplication( argv )
t = QtCore.QTranslator()
t.load( "qt_" + QtCore.QLocale.system().name(), QtCore.QLibraryInfo.location( QtCore.QLibraryInfo.TranslationsPath ) )
a.installTranslator( t )
f = QtWidgets.QFileDialog.getOpenFileName()
if f[0]:
    try:
        w = GraphViewer( [Graph( l.strip() ) for l in open( f[0], "r" ).readlines()] )
        w.show()
        a.exec_()
    except ( IOError, UnicodeDecodeError, Graph.G6Error ):
        QtWidgets.QMessageBox.critical(
            None,
            "Błąd",
            "Wystąpił błąd podczas odczytu z pliku. Upewnij się, że jest on dostępny i zawiera grafy w formacie g6."
        )

