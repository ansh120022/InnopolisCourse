import unittest
from main import calculate, OutOfResourceError

option3 = [
    {
        "ресурс" : "арабика",
        "тип" : "кофе",
        "количество" : 5,
        "порция" : 10
    },
    {
        "ресурс" : "молоко",
        "тип" : "молоко",
        "количество" : 50,
        "порция" : 60
    },
    {
        "ресурс" : "вода",
        "тип" : "вода",
        "количество" : 50,
        "порция" : 60
    }
]


class FunctionalChecker(unittest.TestCase):
    def test_calculate(self):
        self.assertRaises(OutOfResourceError, calculate, option3)


if __name__ == '__main__':
    unittest.main()