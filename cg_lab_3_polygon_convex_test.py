#!/usr/bin/env python

# from basics import * # imported by cg_lab_2_lr_turn_test
# from cg_lab_2_lr_turn import * # imported by cg_lab_2_1_line_segment_intersection
from cg_lab_2_1_line_segment_intersection import *

def is_polygon_convex(polygon):
    """ checks whether given polygon is convex or not
        parameters: list of vertices, number of vertices
        output: boolean
    """
    vertex_list = polygon.vertex_list
    vertex_num = polygon.vertex_num
    is_left_list = [False] * vertex_num
    for index in range(vertex_num):
        # print(index, (index+1)%vertex_num, (index+2)%vertex_num)
        is_left_list[index] = is_left_turn(vertex_list[index], vertex_list[(index+1)%vertex_num], vertex_list[(index+2)%vertex_num])
    # print(is_left_list)

    return True if set(is_left_list) == {True} else False

def is_point_inclusion(polygon, query_point):
    """ checks whether given point is inside given polygon or not
        parameters: list of vertices, query point
        output: boolean
    """
    vertex_list = polygon.vertex_list
    vertex_num = polygon.vertex_num
    is_qpoint_left_turn_list = [False] * vertex_num
    for index in range(vertex_num):
        # print(index, (index+1)%vertex_num, "query_point")
        is_qpoint_left_turn_list[index] = is_left_turn(vertex_list[index], vertex_list[(index+1)%vertex_num], query_point)
    # print(is_qpoint_left_turn_list)

    return True if set(is_qpoint_left_turn_list) == {True} else False

def ray_casting(polygon, ray_line):
    """ checks number of intersection a ray makes with polygon
        parameters: list of vertices, ray_line
        output: number of intersection
    """
    vertex_list = polygon.vertex_list
    vertex_num = polygon.vertex_num
    ray_casting_result = [False] * vertex_num
    for index in range(vertex_num):
        edge = LineSegment(vertex_list[index], vertex_list[(index+1) % vertex_num])
        ray_casting_result[index] = does_lines_intersects(edge, ray_line)
    # print(ray_casting_result)

    return ray_casting_result.count(True)

def main():
    """ Main Function """

    print("CG LAB 3 (Polygon Convex Test)")
    print("Brihat Ratna Bajracharya\n19/075\n")

    ''' get number of vertex for polygon '''
    print("Enter number of vertex of polygon:"),
    vertex_num = int(raw_input())
    # print(vertex_num)

    ''' initialize vertex list '''
    vertex_list = [None] * vertex_num

    ''' get coordinates of each vertices '''
    for index in range(vertex_num):
        print("\n Enter coordinates of vertex V{}".format(index+1))
        vertex_list[index] = Point.input_point()
    # print(vertex_list)

    ''' create polygon from given vertex list '''
    polygon = Polygon(vertex_list)
    print(polygon)

    ''' left turn test using 3 vertex in anti-clockwise '''
    convex_check = is_polygon_convex(polygon)
    print("\nRESULT: Polygon is {}convex.".format('' if convex_check else 'not '))

    if convex_check:
        ''' check point inclusion only if polygon is convex '''
        print("\n\nPOINT INCLUSION BY TURN TEST")
        print("\n Enter coordinates of Query Point (P)")
        query_point = Point.input_point()

        ''' point inclusion using turn test '''
        is_point_in_polygon = is_point_inclusion(polygon, query_point)
        print("\nRESULT: Query Point {}inside given polygon.".format('' if is_point_in_polygon else 'not '))

    print("\n\nRAY CASTING")
    print("\n Enter coordinates of ray point (R)")
    ray_point = Point.input_point()

    ''' assuming ray infinity point to the right side of polygon '''
    ray_xcoord_infinity = max([point.x for point in vertex_list])
    ray_ycoord_infinity = sum([point.y for point in vertex_list]) / vertex_num
    ray_point_infinity = Point(ray_xcoord_infinity * 100, ray_ycoord_infinity)
    ray_line_infinity = LineSegment(ray_point,ray_point_infinity)
    # print(ray_point_infinity)
    # print(ray_line_infinity)

    ''' ray intersection using line_segment_intersection test '''
    ray_intersection_count = ray_casting(polygon, ray_line_infinity)
    ray_casting_result = ray_intersection_count % 2

    print("\nRESULT: Ray origin {} of polygon.".format('inside' if ray_casting_result else 'outside'))
    print("\nDONE.")

if __name__ == '__main__':
    main()
