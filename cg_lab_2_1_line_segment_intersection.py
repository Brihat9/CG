#!/usr/bin/env python

from cg_lab_2_lr_turn import *

def is_point_inbetween(line1_start_point, line1_end_point, query_point):
    """ checks whether query point lies in between start point and end point
        helper function for 'check_improper_intersection' function
    """
    # Case for Line segment parallel to Y-axis
    if line1_start_point.x == line1_end_point.x and line1_start_point.y != line1_end_point.y:
        # case in which query point is in between start point and end point
        if query_point.y > line1_start_point.y and query_point.y < line1_end_point.y:
            return True
    # All other cases
    else:
        # case in which query point is in between start point and end point
        if query_point.x > line1_start_point.x and query_point.x < line1_end_point.x:
            return True
    # if query point not in between start and end point, return False
    return False

def check_improper_intersection(line1_start_point, line1_end_point, query_point, index):
    """ checks improper intersection
        i.e. whether query point (one end of second line)
             just touches the first line
    """
    if is_point_inbetween(line1_start_point, line1_end_point, query_point):
        print(" Improper Intersection")
        print(" Two lines intersect at Point " + index + str(query_point) + "\n"),
    else:
        print(" Two lines do not intersect each other.")

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

def check_proper_intersection(l1_point_a, l1_point_b, l2_point_c, l2_point_d):
    """ checks proper intersection
        i.e. whether second line intersects first line
    """
    l1 = LineSegment(l1_point_a, l1_point_b)
    l2 = LineSegment(l2_point_c, l2_point_d)

    result = does_lines_intersects(l1, l2)
    if result:
        print(" Proper Intersection")
    print(" Two lines do {}intersect each other.".format('' if result else 'not '))

def main():
    """ Main Function """

    print("CG LAB 2.1 (Line Segment Intersection)")
    print("Brihat Ratna Bajracharya\n19/075")

    choice = 'y' # default choice 'yes'
    while(choice == 'y' or choice == 'Y'):
        print("\nEnter coordinates of first line segment (L1)")
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

        print("\n\nRESULT\n------")

        """ end points of two line may be same """
        if l1_point_a == l2_point_c or l1_point_a == l2_point_d:
            print(" Improper Intersection")
            print(" Two lines intersect at Point A" + str(l1_point_a) + "\n")
        elif l1_point_b == l2_point_c or l1_point_b == l2_point_d:
            print(" Improper Intersection")
            print(" Two lines intersect at Point B" + str(l1_point_b) + "\n")
        else:
            """ any one end point may be colinear with other line segment (4 cases) """
            if is_colinear(l1_point_a, l1_point_b, l2_point_c):
                check_improper_intersection(l1_point_a, l1_point_b, l2_point_c, "C")
            elif is_colinear(l1_point_a, l1_point_b, l2_point_d):
                check_improper_intersection(l1_point_a, l1_point_b, l2_point_d, "D")
            elif is_colinear(l2_point_c, l2_point_d, l1_point_a):
                check_improper_intersection(l2_point_c, l2_point_d, l1_point_a, "A")
            elif is_colinear(l2_point_c, l2_point_d, l1_point_b):
                check_improper_intersection(l2_point_c, l2_point_d, l1_point_b, "B")
            else:
                """ if none of end points satisfy colinearity test """
                check_proper_intersection(l1_point_a, l1_point_b, l2_point_c, l2_point_d)

        print("\nDONE.\n")

        ''' Going again if input is 'y', 'Y' or empty '''
        print('Go again? [Y/n]:'),
        choice = raw_input()
        if not choice:
            choice = 'y'

if __name__ == '__main__':
    main()
