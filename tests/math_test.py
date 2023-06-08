import unittest
from math import add, subtract, multiply, divide

class TestArithmeticOperations(unittest.TestCase):

    def test_addition(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = multiply(2, 6)
        self.assertEqual(result, 12)

    def test_division(self):
        result = divide(15, 5)
        self.assertEqual(result, 3)

        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
