#!/usr/bin/env python

from basics import *

def compute_area(base_point, first_point, second_point):
    vecA = Point(first_point.x - base_point.x, first_point.y - base_point.y)
    vecB = Point(second_point.x - base_point.x, second_point.y - base_point.y)

    crossAB = vecA.x * vecB.y - vecA.y * vecB.x

    return crossAB / 2.0

def is_colinear(area):
    return area == 0.0

def is_left_turn(base_point, first_point, second_point):
    area = compute_area(base_point, first_point, second_point)
    return True if area > 0.0 else False

def is_right_turn(base_point, first_point, second_point):
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
    print(" \n Area of triangle P0 P1 P2 is {}".format(area))

    are_points_colinear = is_colinear(area)
    is_left = is_left_turn(base_point, first_point, second_point)
    is_right = is_right_turn(base_point, first_point, second_point)

    print("\n Are points colinear? {}".format(are_points_colinear))
    print(" Is P2 left of P1?    {}".format(is_left))
    print(" Is P2 right of P1?   {}".format(is_right))

    if not are_points_colinear:
        result = "right" if is_right else "left"
        print("\n Point P2 " + str(second_point) + " is in the " + result + " of")
        print(" Point P1 " + str(first_point) + " when observed from")
        print("\b Point P0 " + str(base_point))
    else:
        print(" Point P0 " + str(base_point) + " is colinear with")
        print("\b Point P1 " + str(first_point) + " and Point P2 " + str(second_point))

    print("\nDONE.\n")

if __name__ == '__main__':
    main()
