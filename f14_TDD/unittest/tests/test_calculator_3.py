 #593.5
import unittest
from calculator_module import soma

class TestCalculatorAnyTests(unittest.TestCase):
    
    def test_sum_many_values(self):
        values = ((1,3,4), (1,5,6), (3,5,8))
        for a, b, x in values:
            print(a,b,x)
            self.assertEqual(soma(a,b),x)
        
unittest.main(verbosity=2)