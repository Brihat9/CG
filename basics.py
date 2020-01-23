#!/usr/bin/env python

class Point:
    """ Point Class """

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    @classmethod
    def input_point(point):
        """ Takes X-Coord and Y-Coord from user to form a point """
        return point(
            int(raw_input('  X-Coord: ')),
            int(raw_input('  Y-Coord: ')),
        )

    def __str__(self):
        """ Displays point's coordinates """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        """ Compares two instances of this Class """
        if not isinstance(other, Point):
            # comparision against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return id(self)

class LineSegment:
    """ Line Segment Class """
    def __init__(self, point1, point2):
        self.start = point1
        self.terminal = point2

    def __str__(self):
        """ Displays end-points of line segment """
        return "[" + str(self.start) + ", " + str(self.terminal) + "]"

class Polygon:
    """ Polygon Class """
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.vertex_num = len(vertex_list)

    def __str__(self):
        """ Displays vertices of polygon """
        vertices = "\nPolygon with vertices \n[ "
        for index in range(self.vertex_num):
            vertices += str(self.vertex_list[index]) + " "
        vertices += "]"
        return vertices
