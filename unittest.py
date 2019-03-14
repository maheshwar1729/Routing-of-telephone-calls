#!/usr/bin/python3
import unittest
from main import make_dicts, match_num, operator_name
class TestCase(unittest.TestCase):
    def test_dict(self):
        price = make_dicts("A_op.txt")
        self.assertIsInstance(price, dict)
        self.assertRaises(FileNotFoundError, make_dicts, "invalid.txt")

    def test_match(self):
        match = match_num({'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, \
'4631': 0.15, '4673': 0.9, '46732': 1.1}, "4673212345")
        self.assertEqual(match, {'46732': 1.1})
        self.assertRaises(TypeError, match_num, 342534552)

    def test_match1(self):
        match = match_num({'1': 0.92, '44': 0.5, '46': 0.2, '467': 1.0, '48': 1.2}, "4473212345")
        self.assertEqual(match, {'44': 0.5})

    def test_operator(self):
        operator = operator_name({'4': 0.1}, {'467': 1.0})
        self.assertEqual(operator, "A")

    def test_operator1(self):
        operator = operator_name({'4': 0.1}, {})
        self.assertEqual(operator, "A")

    def test_operator2(self):
        operator = operator_name({}, {})
        self.assertEqual(operator, "None")

if __name__ == '__main__':
    unittest.main()
