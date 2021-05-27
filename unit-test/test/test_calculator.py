import unittest
from ..app import calculator


class TestCalculator(unittest.TestCase):
    """

    """
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(1, 2), -1)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -2), 1)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(1, 2), 2)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(calculator.divide(1, 2), 0.5)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-1, -2), 0.5)

        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()