#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_init(self):
        r = Rectangle(1, 3)
        self.assertEqual(r.id, 1)


    def test_rectangle_init_increment(self):
        r = Rectangle(1, 3)
        r.id += 1
        self.assertEqual(r.id, 2)

    def test_init_with_id(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.id, 1)

    def test_set(self):
        r = Rectangle(1, 3)
        r.width = 5
        r.height = 6
        r.id = 4
        r.x = 3
        r.y = 2
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 4)

    def test_set_errors(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_set_errors2(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.height = "5"

    def test_set_errors3(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.x = "5"

    def test_set_errors4(self):
        r = Rectangle(4, 5)
        with self.assertRaises(TypeError):
            r.y = "5"

    def test_type(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_value_error_1(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

    def test_value_error_2(self):
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)

    def test_value_error_3(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area_rectangle(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area_inf(self):
        import sys
        nb = sys.maxsize + 1
        with self.assertRaises(TypeError):
            r = Rectangle(3, float('inf'))
            self.assertEqual(r.area(), 1)

if __name__ == '__main__':
    unittest.main()
