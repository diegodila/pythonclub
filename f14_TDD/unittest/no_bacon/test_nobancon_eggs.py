'''
TDD - Test driven development

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o codigo e ver o teste passar

Refactor
Parte 3 -> Melhorar meu codigo
'''
import unittest
from nobacon_eggs import nobaconeggs

class TestNOBaconEggs(unittest.TestCase):
    def test_nobacon_eggs_must_raises(self):
        with self.assertRaises(AssertionError):
            nobaconeggs('')
        
        
unittest.main(verbosity=2)