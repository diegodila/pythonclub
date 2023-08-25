#593.4
import unittest
from unittest.calculator_unittest import soma

class TestCalculator(unittest.TestCase):
    def test_sum_35_and_5_should_30(self):
        self.assertEqual(soma(-35,5),-30)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
unittest.TextTestRunner().run(suite)