import unittest
from main import (
    read_file,
    calculate
)


class FunctionalChecker(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(read_file("test_files/1.txt")), 1)
        self.assertEqual(calculate(read_file("test_files/2.txt")), 1)
        self.assertEqual(calculate(read_file("test_files/3.txt")), 2)
        self.assertEqual(calculate(read_file("test_files/4.txt")), 3)
        self.assertEqual(calculate(read_file("test_files/5.txt")), 0)
        self.assertEqual(calculate(read_file("test_files/6.txt")), 1)


if __name__ == '__main__':
    unittest.main()

