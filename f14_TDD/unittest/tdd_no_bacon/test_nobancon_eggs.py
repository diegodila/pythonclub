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
            
    def test_bacon_com_ovos_deve_retornar_alface_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'alface com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    nobaconeggs(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    nobaconeggs(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_algas_se_entrada_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    nobaconeggs(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    nobaconeggs(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                )
        
        
unittest.main(verbosity=2)