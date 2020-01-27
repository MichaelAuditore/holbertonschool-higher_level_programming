#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        c = Base()
        self.assertEqual(c.id, 1)

    def test_init_increment(self):
        c = Base()
        c.id += 1
        self.assertEqual(c.id, 3)


    def test_init_with_id(self):
        c = Base(89)
        self.assertEqual(c.id, 89)

    def test_access_attr(self):
        with self.assertRaises(AttributeError):
            self.assertEqual(Base.__nb_objects, 4)

if __name__ == '__main__':
    unittest.main()
