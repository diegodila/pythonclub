import unittest
from calculator_unittest import soma

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_10(self):
        self.assertEqual(soma(5,5),12)

unittest.main(verbosity=2)