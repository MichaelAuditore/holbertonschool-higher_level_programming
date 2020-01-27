#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_init(self):
        r = Square(1)
        self.assertEqual(r.id, 1)


    def test_square_init_increment(self):
        r = Square(1)
        r.id += 1
        self.assertEqual(r.id, 2)

    def test_init_with_id(self):
        r = Square(3)
        self.assertEqual(r.id, 1)

    def test_set(self):
        r = Square(1)
        r.size = 5
        r.id = 4
        r.x = 3
        r.y = 2
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 4)

    def test_set_errors(self):
        with self.assertRaises(TypeError):
            r = Square("2")

    def test_set_errors2(self):
        r = Square(4)
        with self.assertRaises(TypeError):
            r.size = "5"

    def test_set_errors3(self):
        r = Square(4, 5)
        with self.assertRaises(TypeError):
            r.x = "5"

    def test_set_errors4(self):
        r = Square(4, 5)
        with self.assertRaises(TypeError):
            r.y = "5"

    def test_type(self):
        with self.assertRaises(TypeError):
            r = Square(10)
            r.x = {}

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            r = Square()

    def test_value_error_1(self):
        with self.assertRaises(ValueError):
            r = Square(10)
            r.size = -10

    def test_value_error_2(self):
        with self.assertRaises(TypeError):
            r = Square("4")

    def test_value_error_3(self):
        with self.assertRaises(ValueError):
            r = Square(-10, 2, 3, -1)

    def test_area_rectangle(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_area_inf(self):
        with self.assertRaises(TypeError):
            r = Square(float('inf'))
            self.assertEqual(r.area(), 1)

    def test_print(self):
        r = Square(1)
        sr = "[Square] (1) 0/0 - 1"
        self.assertEqual(r.__str__(), sr)

    def test_str(self):
        r2 = Square(1)
        sr = "[Square] (1) 0/0 - 1"
        self.assertEqual(r2.__str__(), sr)

    def test_print_other(self):
        r = Square(1)
        sr = "[Square] (1) 0/0 - 1"
        self.assertEqual(r.__str__(), sr)

    def test_update(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        sr = "[Square] (89) 3/4 - 2"
        self.assertEqual(r1.__str__(), sr)


    def test_update_kwargs(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(y=1)
        r1.update(size=1, x=2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.id, 10)

if __name__ == '__main__':
    unittest.main()
