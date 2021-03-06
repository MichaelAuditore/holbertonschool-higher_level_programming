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
        with self.assertRaises(TypeError):
            r = Rectangle(3, float('inf'))
            self.assertEqual(r.area(), 1)

    def test_print(self):
        r = Rectangle(1, 2)
        sr = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(r.__str__(), sr)

    def test_str(self):
        r2 = Rectangle(1, 2)
        sr = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(r2.__str__(), sr)

    def test_print_other(self):
        r = Rectangle(1, 2)
        sr = "[Rectangle] (1) 0/0 - 1/2"
        self.assertEqual(r.__str__(), sr)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        r1.update(89, 2, 3, 4, 5)
        sr = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(r1.__str__(), sr)


    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        r1.update(width=1, x=2)
        r1.update(y=1, width=2, x=3, id=89)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.id, 89)



if __name__ == '__main__':
    unittest.main()
