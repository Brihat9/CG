#!/usr/bin/env python

from basics import *

def compute_area(base_point, first_point, second_point):
    """ computes cross product of two vectors to get area of parallelogram
        returns 1/2 of cross product as area of triangle formed
        first vectpr = base point to first point
        second vector = base point to second point
    """
    vecA = Point(first_point.x - base_point.x, first_point.y - base_point.y)
    vecB = Point(second_point.x - base_point.x, second_point.y - base_point.y)

    crossAB = vecA.x * vecB.y - vecA.y * vecB.x

    return crossAB / 2.0

def is_colinear(base_point, first_point, second_point):
    """ checks whether three points are colinear
        using area of triangle == 0 condition
    """
    area = compute_area(base_point, first_point, second_point)
    return area == 0.0

def is_left_turn(base_point, first_point, second_point):
    """ checks whether second point lies on the left of first point
        when seen from base point
    """
    area = compute_area(base_point, first_point, second_point)
    return True if area > 0.0 else False

def is_right_turn(base_point, first_point, second_point):
    """ checks whether second point lies on the right of first point
        when seen from base point
    """
    area = compute_area(base_point, first_point, second_point)
    return True if area < 0.0 else False

def main():
    """ Main Function """

    print("CG LAB 2 (Turn Test)")
    print("Brihat Ratna Bajracharya\n19/075\n")

    print("Enter coordinates of base point (P0)")
    print(" Base Point")
    base_point = Point.input_point()

    print("Enter coordinates of first point (P1)")
    print(" First Point")
    first_point = Point.input_point()

    print("Enter coordinates of second point (P2)")
    print(" Second Point")
    second_point = Point.input_point()

    area = compute_area(base_point, first_point, second_point)
    print(" \n Area of triangle formed by P0 P1 P2 is {0:{1}}"
        .format(area, '+' if area else ''))

    are_points_colinear = is_colinear(base_point, first_point, second_point)
    is_left = is_left_turn(base_point, first_point, second_point)
    is_right = is_right_turn(base_point, first_point, second_point)

    ''' TEST for colinear, left and right '''
    # print("\n Are points colinear? {}".format(are_points_colinear))
    # print(" Is P2 left of P1?    {}".format(is_left))
    # print(" Is P2 right of P1?   {}".format(is_right))

    print("\n\n RESULT\n ------")
    if not are_points_colinear:
        result = "right" if is_right else "left"
        print("\n Point P2 " + str(second_point) + " is in the " + result),
        print("of Point P1 " + str(first_point) + "\n when observed from"),
        print("Point P0 " + str(base_point))
    else:
        print("\n Point P0 " + str(base_point) + " is colinear with"),
        print("Point P1 " + str(first_point)),
        print("and Point P2 " + str(second_point))

    print("\nDONE.\n")

if __name__ == '__main__':
    main()
