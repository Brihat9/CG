#!/usr/bin/env python

from cg_lab_2_lr_turn import *

def does_lines_intersects(line1, line2):
    """ checks whether line1 and line2 crosses each other using turn test """
    is_left_c = is_left_turn(line1.start, line1.terminal, line2.start)
    is_right_c = is_right_turn(line1.start, line1.terminal, line2.start)
    is_left_d = is_left_turn(line1.start, line1.terminal, line2.terminal)
    is_right_d = is_right_turn(line1.start, line1.terminal, line2.terminal)

    """
        IF both ends of line2 lies in same side of line1, no intersection
        IF two ends of line2 lies in opposite site, they should intersect
    """
    res = (is_left_c and is_left_d) or (is_right_c and is_right_d)
    return False if res else True

def main():
    """ Main Function """

    print("CG LAB 2.1 (Line Segment Intersection)")
    print("Brihat Ratna Bajracharya\n19/075\n")

    print("Enter coordinates of first line segment (L1)")
    print(" Enter coordinates of first point (A)")
    print(" Point A of Line L1")
    l1_point_a = Point.input_point()

    print("\n Enter coordinates of second point (B)")
    print(" Point B of line L1")
    l1_point_b = Point.input_point()

    print("\nEnter coordinates of second line segment (L2)")
    print(" Enter coordinates of first point (C)")
    print(" Point C of Line L2")
    l2_point_c = Point.input_point()

    print("\n Enter coordinates of second point (D)")
    print(" Point D of line L2")
    l2_point_d = Point.input_point()

    """ any one end point may be colinear with other line segment (4 cases) """
    if is_colinear(l1_point_a, l1_point_b, l2_point_c):
        print("\nTwo lines intersect at Point C " + str(l2_point_c))
    elif is_colinear(l1_point_a, l1_point_b, l2_point_d):
        print("\nTwo lines intersect at Point D " + str(l2_point_d))
    elif is_colinear(l2_point_c, l2_point_d, l1_point_a):
        print("\nTwo lines intersect at Point A " + str(l2_point_a))
    elif is_colinear(l2_point_c, l2_point_d, l1_point_b):
        print("\nTwo lines intersect at Point B ")
    else:
        """ if none of end points satisfy colinearity test """
        l1 = LineSegment(l1_point_a, l1_point_b)
        l2 = LineSegment(l2_point_c, l2_point_d)

        result = does_lines_intersects(l1, l2)
        print("Two lines do {}intersect each other.".format('' if result else 'not '))

    print("\nDONE.\n")

if __name__ == '__main__':
    main()
