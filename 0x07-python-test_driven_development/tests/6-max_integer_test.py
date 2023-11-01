#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """run test with python3 -m unittest -v tests.6-max_integer_test"""

    def test_area(self):
        self.assertAlmostEqual(max_integer([2, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([-2, -4, -1]), -1)
        self.assertAlmostEqual(max_integer([7]), 7)
        self.assertAlmostEqual(max_integer([7, 8.3]), 8.3)
        self.assertAlmostEqual(max_integer([]), None)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, [2, 's', 3])
        self.assertRaises(TypeError, max_integer, ['s', 3])
        self.assertRaises(TypeError, max_integer, ['2', 3])
        self.assertRaises(TypeError, max_integer, [False, 3])


if __name__ == "__main__":
    unittest.main()
