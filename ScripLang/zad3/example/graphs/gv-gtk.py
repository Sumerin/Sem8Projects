#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przeglądarka grafów, wersja z GUI w GTK.

from gi import require_version

require_version( 'Gtk', '3.0' )

from gi.repository import Gtk
from graphs import Graph
from math import pi, sin, cos


# Główne okno przeglądarki grafów.
class GraphViewer( Gtk.Window ):

    # Tworzy wszystkie komponenty składające się na główne okno przeglądarki grafów.
    def __init__( self, graphs ):
        super().__init__( title = "Przeglądarka grafów", window_position = Gtk.WindowPosition.CENTER )
        self.__graphs = graphs
        self.__index = 0
        self.__graph_label = Gtk.Label( label = "<b>" + self.__graphs[self.__index].g6() + "</b>", use_markup = True )
        self.__graph_view = Gtk.DrawingArea()
        self.__next_button = Gtk.Button( image = Gtk.Image.new_from_icon_name( "go-next", Gtk.IconSize.BUTTON ) )
        self.__previous_button = Gtk.Button( image = Gtk.Image.new_from_icon_name( "go-previous", Gtk.IconSize.BUTTON ) )
        self.__progress_label = Gtk.Label( label = "1 / " + str( len( self.__graphs ) ) )
        self.__previous_button.set_sensitive( False )
        self.__previous_button.connect( "clicked", self.__show_previous_graph )
        if len( self.__graphs ) == 1:
            self.__next_button.set_sensitive( False )
        self.__next_button.connect( "clicked", self.__show_next_graph )
        self.__graph_view.connect( "draw", self.__draw_graph )
        self.__graph_view.set_size_request( 320, 200 )
        b1 = Gtk.Box( orientation = Gtk.Orientation.VERTICAL, homogeneous = False )
        b1.pack_start( self.__graph_label, False, True, 0 )
        b1.pack_start( self.__graph_view, True, True, 0 )
        b2 = Gtk.Box( orientation = Gtk.Orientation.HORIZONTAL, homogeneous = False )
        b2.pack_start( self.__previous_button, False, True, 12 )
        b2.pack_start( self.__progress_label, True, True, 0 )
        b2.pack_start( self.__next_button, False, True, 12 )
        b1.pack_start( b2, False, True, 8 )
        self.add( b1 )
        self.set_default_size( 800, 600 )

    # Pokazuje następny graf.
    def __show_next_graph( self, button ):
        self.__index += 1
        self.__previous_button.set_sensitive( True )
        if len( self.__graphs ) == self.__index + 1:
            self.__next_button.set_sensitive( False )
        self.__graph_label.set_label( "<b>" + self.__graphs[self.__index].g6() + "</b>" )
        self.__progress_label.set_label( str( self.__index + 1 ) + " / " + str( len( self.__graphs ) ) )
        self.queue_draw()

    # Pokazuje poprzedni graf.
    def __show_previous_graph( self, button ):
        self.__index -= 1
        self.__next_button.set_sensitive( True )
        if self.__index == 0:
            self.__previous_button.set_sensitive( False )
        self.__graph_label.set_label( "<b>" + self.__graphs[self.__index].g6() + "</b>" )
        self.__progress_label.set_label( str( self.__index + 1 ) + " / " + str( len( self.__graphs ) ) )
        self.queue_draw()

    # Przerysowuje aktualnie pokazywany graf.
    def __draw_graph( self, widget, context ):
        w, h = self.__graph_view.get_allocated_width(), self.__graph_view.get_allocated_height()
        r = 0.45 * min( w, h )
        o = self.__graphs[self.__index].order()
        context.set_source_rgb( 0.4, 0.6, 0.8 )
        for i,j in self.__graphs[self.__index].edges():
            xi = (w / 2) + cos( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            yi = (h / 2) + sin( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            context.move_to( xi, yi )
            xj = (w / 2) + cos( 2 * pi * (j / o) + 3 * pi / 2 ) * r
            yj = (h / 2) + sin( 2 * pi * (j / o) + 3 * pi / 2 ) * r
            context.line_to( xj, yj )
            context.stroke()
        context.set_source_rgb( 0.8, 0.5, 0.4 )
        for i in range( o ):
            x = (w / 2) + cos( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            y = (h / 2) + sin( 2 * pi * (i / o) + 3 * pi / 2 ) * r
            context.arc( x, y, r / 25, 0, 2 * pi )
            context.fill()

# Główna część programu.
d = Gtk.FileChooserDialog(
    title = "Wybierz plik z grafami",
    action = Gtk.FileChooserAction.OPEN,
    buttons = ( "Zatwierdź", Gtk.ResponseType.OK, "Anuluj", Gtk.ResponseType.CANCEL )
)
if d.run() == Gtk.ResponseType.OK:
    d.hide()
    try:
        w = GraphViewer( [Graph( l.strip() ) for l in open( d.get_filename(), "r" ).readlines()] )
        w.connect( "delete-event", Gtk.main_quit )
        w.show_all()
        Gtk.main()
    except ( IOError, UnicodeDecodeError, Graph.G6Error ):
        Gtk.MessageDialog(
            title = "Błąd",
            text = "Wystąpił błąd podczas odczytu z pliku. Upewnij się, że jest on dostępny i zawiera grafy w formacie g6.",
            message_type = Gtk.MessageType.ERROR,
            buttons = ( "Ok", Gtk.ButtonsType.OK )
        ).run()
