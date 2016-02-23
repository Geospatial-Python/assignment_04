import os
import random
import sys
import unittest

sys.path.append(os.path.abspath('..'))

from .. import point_pattern


class TestFilesAndDicts(unittest.TestCase):
    """
    This set of tests is focused on reading some geojson
    data in as a Python dictionary and then answering
    some questions about the data.
    """

    @classmethod
    def setUpClass(cls):
        cls.gj = point_pattern.read_geojson('data/us_cities.geojson')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

    def test_find_largest(self):
        city, pop = point_pattern.find_largest_city(self.gj)
        self.assertEqual(city, 'New York')
        self.assertEqual(pop, 19040000)

    def test_write_your_own(self):
        """
        Here you will write a test for the code you write in
        point_pattern.py.
        """
        some_return = point_pattern.write_your_own(self.gj)
        self.assertTrue(some_return, 55)

class TestIterablePointPattern(unittest.TestCase):
    """
    This set of tests is focused on iterables and sequences.  Once
    passing, you will have the foundation of some point pattern analysis
    functionality.
    """
    # This is like the standard setup, except it is only called once
    @classmethod
    def setUpClass(cls):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        cls.points = [(random.randint(0,100), random.randint(0,100)) for i in range(50)]

    def test_average_nearest_neighbor_distance(self):
        mean_d = point_pattern.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(mean_d, 7.629178, 5)

    def test_mean_center(self):
        """
        Something to think about - What values would you
         expect to see here and why?  Why are the values
         not what you might expect?
        """
        x, y = point_pattern.mean_center(self.points)
        self.assertEqual(x, 47.52)
        self.assertEqual(y, 45.14)

    def test_minimum_bounding_rectangle(self):
        mbr = point_pattern.minimum_bounding_rectangle(self.points)
        self.assertEqual(mbr, [0,0,94,98])

    def test_mbr_area(self):
        mbr = [0,0,94,98]
        area = point_pattern.mbr_area(mbr)
        self.assertEqual(area, 9212)

    def test_expected_distance(self):
        area = 9212
        npoints = 50
        expected = point_pattern.expected_distance(area, npoints)
        self.assertAlmostEqual(expected, 6.7867518, 5)


class TestPointPattern(unittest.TestCase):
    """
    These are the tests that you got working in assignment 3.
    You should not need to alter these at all.
    """
    def setUp(self):
        pass

    def test_getx(self):
        """
        A simple test to ensure that you understand how to access
        the x coordinate in a tuple of coordinates.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `getx` function so that the correct
        values are returned.
        """
        point = (1,2)
        x = point_pattern.getx(point)
        self.assertEqual(1, x)

    def test_gety(self):
        """
        As above, except get the y coordinate.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `gety` function so that the correct
        values are returned.
        """
        point = (3,2.5)
        y = point_pattern.gety(point)
        self.assertEqual(2.5, y)

    def test_shift_point(self):
        """
        Test that a point is being properly shifted
         when calling point_pattern.shift_point
        """
        point = (0,0)
        new_point = point_pattern.shift_point(point, 3, 4)
        self.assertEqual((3,4), new_point)

        point = (-2.34, 1.19)
        new_point = point_pattern.shift_point(point, 2.34, -1.19)
        self.assertEqual((0,0), new_point)

    def test_euclidean_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = point_pattern.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(2.8284271, distance, 4)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = point_pattern.euclidean_distance(point_a, point_b)
        self.assertAlmostEqual(7.7074639, distance, 4)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = point_pattern.euclidean_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_manhattan_distance(self):
        """
        A test to ensure that the distance between points
        is being properly computed.

        You do not need to make any changes to this test,
        instead, in point_pattern.py, you must complete the
        `eucliden_distance` function so that the correct
        values are returned.

        Something to think about: Why might you want to test
        different cases, e.g. all positive integers, positive
        and negative floats, coincident points?
        """
        point_a = (3, 7)
        point_b = (1, 9)
        distance = point_pattern.manhattan_distance(point_a, point_b)
        self.assertEqual(4.0, distance)

        point_a = (-1.25, 2.35)
        point_b = (4.2, -3.1)
        distance = point_pattern.manhattan_distance(point_a, point_b)
        self.assertEqual(10.9, distance)

        point_a = (0, 0)
        point_b = (0, 0)
        distance = point_pattern.manhattan_distance(point_b, point_a)
        self.assertAlmostEqual(0.0, distance, 4)

    def test_check_coincident(self):
        """
        As above, update the function in point_pattern.py

        """
        point_a = (3, 7)
        point_b = (3, 7)
        coincident = point_pattern.check_coincident(point_a, point_b)
        self.assertEqual(coincident, True)

        point_b = (-3, -7)
        coincident = point_pattern.check_coincident(point_a, point_b)
        self.assertEqual(coincident, False)

        point_a = (0, 0)
        point_b = (0.0, 0.0)
        coincident = point_pattern.check_coincident(point_b, point_a)
        self.assertEqual(coincident, True)

    def test_check_in(self):
        """
        As above, update the function in point_pattern.py
        """
        point_list = [(0,0), (1,0.1), (-2.1, 1),
                      (2,4), (1,1), (3.5, 2)]

        inlist = point_pattern.check_in((0,0), point_list)
        self.assertTrue(inlist)

        inlist = point_pattern.check_in((6,4), point_list)
        self.assertFalse(inlist)
