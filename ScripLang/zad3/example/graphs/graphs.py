#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Graf reprezentowany w postaci listy krawędzi.
class Graph:

    # Wyjątek pojawiający się przy próbie utworzenia grafu z napisu niezgodnego z formatem g6.
    class G6Error( Exception ): pass

    # Tworzy nowy graf, odczytując liczbę wierzchołków oraz krawędzie z podanego napisu (w formacie g6).
    def __init__( self, text ):
        self.__g6 = text
        try:
            o, e = text[0], text[1:]
            self.__order = self.__read_order( o )
            self.__edges = self.__read_edges( e )
        except ValueError:
            raise Graph.G6Error

    # Odczytuje liczbę wierzchołków z podanego fragmentu napisu w formacie g6.
    def __read_order( self, text ):
        if len( text ) != 1 or ord( text[0] ) < 63 or ord( text[0] ) > 125:
            raise Graph.G6Error
        return ord( text[0] ) - 63

    # Odczytuje krawędzie grafu z podanego fragmentu napisu w formacie g6.
    def __read_edges( self, text ):
        e, k, t = [], 0, iter( text )
        for j in range( 1, self.__order ):
            for i in range( j ):
                if k == 0:
                    try:
                        c = ord( next( t ) ) - 63
                    except StopIteration:
                        raise Graph.G6Error
                    if c < 0 or c > 63:
                        raise Graph.G6Error
                    k = 6
                k -= 1
                if (c & (1 << k)) != 0:
                    e.append( ( i, j ) )
        try:
            next( t )
            raise Graph.G6Error
        except StopIteration:
            return e

    # Zwraca graf zapisany w formacie g6.
    def g6( self ):
        return self.__g6

    # Zwraca listę krawędzi grafu.
    def edges( self ):
        return self.__edges

    # Zwraca liczbę wierzchołków grafu.
    def order( self ):
        return self.__order
