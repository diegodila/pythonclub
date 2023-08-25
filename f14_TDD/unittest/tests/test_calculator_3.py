
from setuptools import setup, find_packages
setup(name = 'soma', packages = find_packages())

#593.5
from calculator_unittest import soma

class TestCalculatorAnyTests(unittest.TestCase):
    def sum_many_values(self):
        values = ((1,3,4), (1,5,6), (3,5,8))
        for a, b, x in values:
            print(a,b,x)
            self.assertEqual(soma(a,b),x)
        
unittest.main(verbosity=2)