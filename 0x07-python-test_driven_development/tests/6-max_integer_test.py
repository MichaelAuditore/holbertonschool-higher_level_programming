#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

    def test_neg_pos(self):
        self.assertEqual(max_integer([-1, 3, 5, -7]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_string_into(self):
        self.assertEqual(max_integer("Miguel"), "u")

    def test_more_strings(self):
        self.assertEqual(max_integer(("Canon")), "o")

    def test_floats(self):
        self.assertEqual(max_integer([10.2, 2.2, 3.4, 4.5]), 10.2)

    def test_neg_floats(self):
        self.assertEqual(max_integer([-1.3, -10.2, -15.3]), -1.3)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_same_numbers(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_same_neg_numbers(self):
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

    def test_integer_number(self):
        self.assertEqual(max_integer([2]), 2)

    def test_tuples(self):
        self.assertEqual(max_integer((9, 3, 4)), 9)

    def test_comprehension(self):
        self.assertEqual(max_integer([i for i in range(10)]), 9)

    def test_letters_into(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer([1, 2, 'a']), 'a')

if __name__ == '__main__':
    unittest.main()
