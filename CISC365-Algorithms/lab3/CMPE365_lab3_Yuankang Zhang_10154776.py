import random
import math
import numpy

# creating a number of sets of uniformly distributed points


def create_uniformly_points(set):
    # point sets
    point_sets = []
    circle_set = []

    for i in range(set):
        # create radius of the circles
        circle_r = random.random() * 30
        # create an origin
        circle_x = random.random() * 30
        circle_y = random.random() * 30
        circle_set.append([circle_r, circle_x, circle_y])
        # random angle
        theta = 2 * math.pi * random.random()
        # create points
        points = []
        num = int(random.random() * 30)
        for i in range(num):
            # random radius
            r = circle_r * math.sqrt(random.random())
            x = r * math.cos(theta) + circle_x
            y = r * math.sin(theta) + circle_y
            points.append([x, y])
        # put in the point_sets
        point_sets.append(points)

    return point_sets, circle_set


def create_gaussian_points(set, num):
    mu = 30
    sigma = 3
    # point sets
    point_sets = []
    
    for i in range(set):
        # create radius of the circles
        circle_r = random.random() * 30
        # create an origin
        circle_x = random.random() * 30
        circle_y = random.random() * 30
        # random angle
        theta = 2 * math.pi * random.random()
        # create points
        points = []
        for i in range(num):
            # random radius
            circle_r = numpy.random.normal(mu, sigma, (1, 1))
            r = circle_r * math.sqrt(random.random())
            x = r * math.cos(theta) + circle_x
            y = r * math.sin(theta) + circle_y
            points.append([x, y])
        # put in the point_sets
        point_sets.append(points)

    return point_sets


# Implement Quickhull algorithms
# When called returns a list of points that forms a convex hull around
# the listPts Given
def get_hull_points(listPts):
    min, max = get_min_max_x(listPts)

    hull_points = quickhull(listPts, min, max)
    hull_points = hull_points + quickhull(listPts, max, min)

    return hull_points


# Does the sorting for the quick hull sorting algorithm
def quickhull(listPts, min, max):
    left_of_line_pts = get_points_left_of_line(min, max, listPts)
    ptC = point_max_from_line(min, max, left_of_line_pts)

    if len(ptC) < 1:
        return [max]
    hull_points = quickhull(left_of_line_pts, min, ptC)
    hull_points = hull_points + quickhull(left_of_line_pts, ptC, max)

    return hull_points


# Reterns all points that a LEFT of a line start->end
def get_points_left_of_line(start, end, listPts):
    pts = []

    for pt in listPts:
        if isCounterClockWise(start, end, pt):
            pts.append(pt)

    return pts


#Returns the maximum point from a line start->end
def point_max_from_line(start, end, points):
    max_dist = 0
    max_point = []

    for point in points:
        if point != start and point != end:
            dist = distance(start, end, point)
            if dist > max_dist:
                max_dist = dist
                max_point = point

    return max_point


#Returns the maximum point from a line start->end
def get_min_max_x(list_pts):
    min_x = float('inf')
    max_x = 0
    min_y = 0
    max_y = 0
    for i in list_pts:
        if i[0] < min_x:
            min_x = i[0]
            min_y = i[1]
        if i[0] > max_x:
            max_x = i[0]
            max_y = i[1]
    return [min_x,min_y], [max_x,max_y]


# Given a line of start->end, will return the distance that
# point, pt, is from the line.
def distance(start, end, pt):
    x1, y1 = start
    x2, y2 = end
    x0, y0 = pt
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = nom / denom
    return result


def isCounterClockWise(start, end, pt):
    slope = float(end[1] - start[1]) / float(end[0] - start[0])
    if slope >= 0:
        if pt[0] < start[0]:
            if pt[1] > (start[1] - abs(pt[0]-start[0])*slope):
                return True
            else:
                return False
        else:
            if pt[1] > (start[1] + abs(pt[0]-start[0])*slope):
                return True
            else:
                return False
    else:
        if pt[0] < start[0]:
            if pt[1] < (start[1] - abs(pt[0]-start[0])*slope):
                return True
            else:
                return False
        else:
            if pt[1] < (start[1] + abs(pt[0]-start[0])*slope):
                return True
            else:
                return False


# Performing Quickhull and calculate the average ratio of convex hull size to number of points
def cal_ratio(sets_of_points):
    ratio = []
    ratio_sum = 0
    
    for i in range(len(sets_of_points)):
        new_hull_points = get_hull_points(sets_of_points[i])
        a_ratio = float(len(new_hull_points)) / float(len(sets_of_points[i]))
        ratio.append(a_ratio)

    for i in ratio:
        ratio_sum = ratio_sum + i

    average_ratio = ratio_sum / len(sets_of_points)

    print (ratio)
    print (average_ratio)    

# Attempt for intersection check
# def ifOverlaped(circles):


# tests
def test_uniformly():
    new_sets_of_points, circles = create_uniformly_points(10)
    cal_ratio(new_sets_of_points)
    # Attempt for intersection check
    # if ifOverlaped(circles):
    #    print ("Overlapped")


def test_gaussian():
    new_sets_of_points = create_gaussian_points(10, 10)
    cal_ratio(new_sets_of_points)


test_uniformly()

test_gaussian()
