import unittest
from task1 import sumOfRange


class TestTask1(unittest.TestCase):

    def test_basic_1(self):
        self.assertEqual(sumOfRange(1), 1)

    def test_basic_2(self):
        self.assertEqual(sumOfRange(3), 6)

    def test_basic_3(self):
        self.assertEqual(sumOfRange(10), 55)

    def test_wrong_type_string(self):
        with self.assertRaises(TypeError):
            sumOfRange("fsgs")

    def test_wrong_type_decimal(self):
        with self.assertRaises(TypeError):
            sumOfRange(1.0)

    def test_out_of_limits_1(self):
        with self.assertRaises(ValueError):
            sumOfRange(0)

    def test_out_of_limits_2(self):
        with self.assertRaises(ValueError):
            sumOfRange(-3)

    def test_out_of_limits_3(self):
        with self.assertRaises(ValueError):
            sumOfRange(10 ** 26)


if __name__ == '__main__':
    unittest.main()
