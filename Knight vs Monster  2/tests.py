"""Юнит-тесты некоторых функций."""

import unittest
from validation import valid_input


class FunctionalChecker(unittest.TestCase):
    """Проверка функции valid_input."""
    def test_calculate(self):
        """Проверка функции valid_input."""
        self.assertEqual(False, valid_input('a'))
        self.assertEqual(False, valid_input(' '))
        self.assertEqual(True, valid_input('3'))


if __name__ == '__main__':
    unittest.main()
