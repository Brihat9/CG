#!/usr/bin/env python

from basics import Point, LineSegment
from circular_doubly_linked_list import CircularDoublyLinkedList
from cg_lab_2_lr_turn import is_left_turn
from cg_lab_2_1_line_segment_intersection import does_lines_intersect

import copy
import math

''' change input file here '''
INPUT_FILE = 'cg_lab_3_input_file_1'

def is_polygon_convex(polygon):
    """ checks whether given polygon is convex or not
        parameters: Polygon
        output: boolean
    """
    vertex_num = polygon.get_count()
    is_left_list = [False] * vertex_num

    cursor = polygon.head
    for index in range(vertex_num):
        is_left_list[index] = is_left_turn(cursor.data, cursor.next.data, cursor.next.next.data)
        cursor = cursor.next
    # print(is_left_list)

    return True if set(is_left_list) == {True} else False

def is_point_inclusion(polygon, query_point):
    """ checks whether given point is inside given polygon or not
        parameters: Polygon, query point
        output: boolean
    """
    vertex_num = polygon.get_count()
    is_qpoint_left_turn_list = [False] * vertex_num

    cursor = polygon.head
    for index in range(vertex_num):
        # print(index, (index+1)%vertex_num, "query_point")
        is_qpoint_left_turn_list[index] = is_left_turn(cursor.data, cursor.next.data, query_point)
        cursor = cursor.next
    # print(is_qpoint_left_turn_list)

    return True if set(is_qpoint_left_turn_list) == {True} else False

def ray_casting(polygon, ray_line):
    """ checks number of intersection a ray makes with polygon
        parameters: Polygon, ray (line)
        output: number of intersection
    """
    vertex_num = polygon.get_count()
    ray_casting_result = [False] * vertex_num

    cursor = polygon.head
    for index in range(vertex_num):
        edge = LineSegment(cursor.data, cursor.next.data)
        ray_casting_result[index] = does_lines_intersect(edge, ray_line)
        cursor = cursor.next
    # print(ray_casting_result)
    return ray_casting_result.count(True)

def main():
    # print("LAB3")
    """ Main Function """

    print("CG LAB 3")
    print("Brihat Ratna Bajracharya\n19/075\n")

    try:
        ''' reads input file '''
        in_file = open(INPUT_FILE, 'r')

        ''' get number of vertices for polygon '''
        print("Enter number of vertex of polygon:"),
        vertex_num = int(in_file.readline())
        print(vertex_num)

        ''' reads coords of point '''
        input_coords = in_file.readline()
        input_coords_list = input_coords.split()
        # print(input_coords_list)

        ''' initialize vertex list '''
        points = [None] * vertex_num

        ''' get coordinates of each vertices '''
        for index in range(vertex_num):
            print(" Enter coordinates of vertex V{}:".format(index+1)),
            input_coords_point = input_coords_list[index].split(',')
            points[index] = Point(int(input_coords_point[0]), int(input_coords_point[1]))
            print(points[index])

        ''' calculate centroid of polygon '''
        centroid = Point(sum([point.x for point in points])/len(points),sum([point.y for point in points])/len(points))
        # print("Centroid of all Points: " + str(centroid))

        ''' sort vertices of polygon in anti-clockwise order '''
        sorted_p = copy.deepcopy(points)
        sorted_p.sort(key=lambda p: math.atan2(p.y-centroid.y,p.x-centroid.x))

        ''' show points in sorted order '''
        # print("\nPoints in sorted order")
        # for index in range(vertex_num):
        #     print(sorted_p[index]),
        # print("\n")

        polygon = CircularDoublyLinkedList()
        for index in range(vertex_num):
            polygon.append(sorted_p[index])

        ''' displays content of polygon and count of vertices '''
        polygon.display("Vertices of Polygon (sorted)")
        # polygon.show_count()


        ''' polygon convex test '''
        convex_check = is_polygon_convex(polygon)
        print("\nRESULT: Polygon is {}convex.".format('' if convex_check else 'not '))


        if convex_check:
            ''' check point inclusion only if polygon is convex '''
            print("\n\nPOINT INCLUSION BY TURN TEST")
            print("\n Enter coordinates of Query Point (P):"),

            ''' read query point from file '''
            qp = in_file.readline().split()[0].split(',')
            # print(qp)

            query_point =  Point(int(qp[0]), int(qp[1]))
            print(query_point)

            ''' point inclusion using turn test '''
            is_point_in_polygon = is_point_inclusion(polygon, query_point)
            print("\nRESULT: Query Point {}inside given polygon.".format('' if is_point_in_polygon else 'not '))

        print("\n\nRAY CASTING")
        print("\n Enter coordinates of ray point (R):"),

        ''' read ray point start from file '''
        if not convex_check:
            in_file.readline()
        rp = in_file.readline().split()[0].split(',')
        # print(rp)

        ray_point =  Point(int(rp[0]), int(rp[1]))
        print(ray_point)

        ''' assuming ray infinity point to the right side of polygon '''
        ray_xcoord_infinity = max([point.x for point in sorted_p])
        ray_ycoord_infinity = sum([point.y for point in sorted_p]) / vertex_num
        ray_point_infinity = Point(ray_xcoord_infinity * 100, ray_ycoord_infinity)
        ray_line_infinity = LineSegment(ray_point,ray_point_infinity)
        # print("\n  Ray Point Infinity: " + str(ray_point_infinity))
        # print("  Ray Line: " + str(ray_line_infinity))

        ''' ray intersection using line_segment_intersection test '''
        ray_intersection_count = ray_casting(polygon, ray_line_infinity)
        ray_casting_result = ray_intersection_count % 2

        print("\nRESULT: Ray origin {} of polygon.".format('inside' if ray_casting_result else 'outside'))

        in_file.close()
        print("\nDONE.")

    except Exception as e:
        print("\n\nERROR OCCURED !!!\n Type of Error:  " + type(e).__name__)
        print(" Error message:  " + str(e.message))


if __name__ == '__main__':
    main()
