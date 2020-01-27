#!/usr/bin/python3
"""Unittest for class Base()
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        c = Base()
        self.assertEqual(c.id, 1)

    def test_init_increment(self):
        d = Base()
        d.id += 1
        self.assertEqual(d.id, 2)


    def test_init_with_id(self):
        e = Base(89)
        self.assertEqual(e.id, 89)


if __name__ == '__main__':
    unittest.main()
