import math  # I am guessing that you will need to use the math module
import json  # I would like you to use the JSON module for reading geojson (for now)
"""
Like last assignment, we are going to be working with point
patterns.  The readings focused on iteration, sequences, and
conditional execution.  We are going to use these concepts
to write functions to:
1. Read a geojson file
2. Parse a geojson file to find the largest city by population
3. Write your own code to do something interesting with the geojson
4. Compute the mean center of a point pattern
5. Compute the average distance between neighbors
6. Compute the miminum bounding rectangle (MBR) on a point pattern
7. Compute the area of a MBR
8. Compute the expected mean distance for a given point pattern
"""


def read_geojson(input_file):
    """
    Read a geojson file
    Parameters
    ----------
    input_file : str
                 The PATH to the data to be read
    Returns
    -------
    gj : dict
         An in memory version of the geojson
    """
    # Please use the python json module (imported above)
    # to solve this one.
    with open ('data/us_cities.geojson', 'r') as f:
        gj = json.load(f)
    gj = ['features']    
    print (gj[feature[10]['type']['pop_max']
    #return gj


def find_largest_city(gj):
    """
    Iterate through a geojson feature collection and
    find the largest city.  Assume that the key
    to access the maximum population is 'pop_max'.
    Parameters
    ----------
    gj : dict
         A GeoJSON file read in as a Python dictionary
    Returns
    -------
    city : str
           The largest city
    population : int
                 The population of the largest city
    """
    
    temp = 0
    for i in gj:
       if i['pop_max'] > temp:
            temp = i['pop_max']
            city = i['city']
            max_population = temp

    return city, max_population


def write_your_own(gj):
    """
    Here you will write your own code to find
    some attribute in the supplied geojson file.
    Take a look at the attributes available and pick
    something interesting that you might like to find
    or summarize.  This is totally up to you.
    Do not forget to write the accompanying test in
    tests.py!
    """
    temp = 0
    for i in gj:
        if i['pop_min'] < temp:
            temp = i['pop_min']
            city = i['city']
            min_population = temp

    return city, min_population

def mean_center(points):
    """
    Given a set of points, compute the mean center
    Parameters
    ----------
    points : list
         A list of points in the form (x,y)
    Returns
    -------
    x : float
        Mean x coordinate
    y : float
        Mean y coordinate
    """

    summation_x = 0
    summation_y = 0
    for i in points:
        summation_x += i[0]
        summation_y += i[1]

    x = float(summation_x / len(points))
    y = float(summation_y / len(points))

    return x, y


def average_nearest_neighbor_distance(points):
    """
    Given a set of points, compute the average nearest neighbor.
    Parameters
    ----------
    points : list
             A list of points in the form (x,y)
    Returns
    -------
    mean_d : float
             Average nearest neighbor distance
    References
    ----------
    Clark and Evan (1954 Distance to Nearest Neighbor as a
     Measure of Spatial Relationships in Populations. Ecology. 35(4)
     p. 445-453.
    """


    mean_d = mean_center(points) / len(points)

    return mean_d


def minimum_bounding_rectangle(points):
    """
    Given a set of points, compute the minimum bounding rectangle.
    Parameters
    ----------
    points : list
             A list of points in the form (x,y)
    Returns
    -------
     : list
       Corners of the MBR in the form [xmin, ymin, xmax, ymax]
    """

    xmin = min(points[0])
    ymin = min(points[1])
    xmax = max(points[0])
    ymax = max(points[1])

    mbr = [xmin,ymin,xmax,ymax]

    return mbr


def mbr_area(mbr):
    """
    Compute the area of a minimum bounding rectangle
    """
    area = (mbr[2] - mbr[0]) * (mbr[3] - mbr[1])

    return area


def expected_distance(area, n):
    """
    Compute the expected mean distance given
    some study area.
    This makes lots of assumptions and is not
    necessarily how you would want to compute
    this.  This is just an example of the full
    analysis pipe, e.g. compute the mean distance
    and the expected mean distance.
    Parameters
    ----------
    area : float
           The area of the study area
    n : int
        The number of points
    """

    expected = .5 / ((math.sqrt(n/area)))
    return expected


"""
Below are the functions that you created last week.
Your syntax might have been different (which is awesome),
but the functionality is identical.  No need to touch
these unless you are interested in another way of solving
the assignment
"""

def manhattan_distance(a, b):
    """
    Compute the Manhattan distance between two points
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)
    b : tuple
        A point in the form (x,y)
    Returns
    -------
    distance : float
               The Manhattan distance between the two points
    """
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def euclidean_distance(a, b):
    """
    Compute the Euclidean distance between two points
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)
    b : tuple
        A point in the form (x,y)
    Returns
    -------
    distance : float
               The Euclidean distance between the two points
    """
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance


def shift_point(point, x_shift, y_shift):
    """
    Shift a point by some amount in the x and y directions
    Parameters
    ----------
    point : tuple
            in the form (x,y)
    x_shift : int or float
              distance to shift in the x direction
    y_shift : int or float
              distance to shift in the y direction
    Returns
    -------
    new_x : int or float
            shited x coordinate
    new_y : int or float
            shifted y coordinate
    Note that the new_x new_y elements are returned as a tuple
    Example
    -------
    >>> point = (0,0)
    >>> shift_point(point, 1, 2)
    (1,2)
    """
    x = getx(point)
    y = gety(point)

    x += x_shift
    y += y_shift

    return x, y


def check_coincident(a, b):
    """
    Check whether two points are coincident
    Parameters
    ----------
    a : tuple
        A point in the form (x,y)
    b : tuple
        A point in the form (x,y)
    Returns
    -------
    equal : bool
            Whether the points are equal
    """
    return a == b


def check_in(point, point_list):
    """
    Check whether point is in the point list
    Parameters
    ----------
    point : tuple
            In the form (x,y)
    point_list : list
                 in the form [point, point_1, point_2, ..., point_n]
    """
    return point in point_list


def getx(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.
    Parameters
    ----------
    point : tuple
            in the form (x,y)
    Returns
    -------
     : int or float
       x coordinate
    """
    return point[0]


def gety(point):
    """
    A simple method to return the x coordinate of
     an tuple in the form(x,y).  We will look at
     sequences in a coming lesson.
    Parameters
    ----------
    point : tuple
            in the form (x,y)
    Returns
    -------
     : int or float
       y coordinate
    """
    return point[1]
