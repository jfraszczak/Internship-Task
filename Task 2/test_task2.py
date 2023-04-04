import unittest
from task2 import IslandsCounter


class TestTask2(unittest.TestCase):

    def test_1(self):
        islands_map = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1]
        ]

        islands_counter = IslandsCounter(islands_map)
        islands_counter.count()

        self.assertEqual(islands_counter.getNumberOfIslands(), 2)

    def test_2(self):
        islands_map = [
            [0, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 1]
        ]

        islands_counter = IslandsCounter(islands_map)
        islands_counter.count()

        self.assertEqual(islands_counter.getNumberOfIslands(), 2)

    def test_3(self):
        islands_map = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0]
        ]

        islands_counter = IslandsCounter(islands_map)
        islands_counter.count()

        self.assertEqual(islands_counter.getNumberOfIslands(), 3)


if __name__ == '__main__':
    unittest.main()
