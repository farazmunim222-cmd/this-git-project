import unittest

from grade_calculator import (
    calculate_average,
    get_grade,
    is_pass,
    get_highest_mark
)


class TestGradeCalculator(unittest.TestCase):

    def test_get_grade_85(self):
        self.assertEqual(get_grade(85), 'A+')

    def test_get_grade_35(self):
        self.assertEqual(get_grade(35), 'F')

    def test_get_grade_100(self):
        self.assertEqual(get_grade(100), 'A+')

    def test_get_grade_negative_value_error(self):
        with self.assertRaises(ValueError):
            get_grade(-5)

    def test_get_grade_invalid_value_error(self):
        with self.assertRaises(ValueError):
            get_grade(110)

    def test_get_grade_type_error(self):
        with self.assertRaises(TypeError):
            get_grade(None)

    def test_is_pass_40(self):
        self.assertTrue(is_pass(40))

    def test_is_pass_25(self):
        self.assertFalse(is_pass(25))

    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_get_highest_mark(self):
        self.assertEqual(get_highest_mark([45, 88, 67]), 88)


if __name__ == '__main__':
    unittest.main()
