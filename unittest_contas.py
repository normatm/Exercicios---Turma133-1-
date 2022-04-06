# 1 - Bibliotecas
import unittest # Essa biblioteca será baixada automaticamente pelo PIP
import main     # referencia ao arquivo main.py

# 2 - Classes (Grupo de Definitions)
class Casos_De_Teste(unittest.TestCase):
    # 3 - Métodos e Funções
    lista_para_multiplicar =
        (2, 3, 6),
        (0, 4, 0)
        (-5, -3, 15)
    def test_multiplicar_2_numeros(self):
        # A -  Configura
        numero1 = 4
        numero2 = 8
        resultado_esperado = 32

        # B - Executa
        resultado_obtido = main.multiplicar_2_numeros(numero1, numero2)

        # C - Valida
        self.assertEqual(resultado_esperado, resultado_obtido)  # add assertion here

    def test_somar_2_numeros(self):
        numero1 = 7
        numero2 = 8
        resultado_esperado = 15

        resultado_obtido = main.somar_2_numeros(numero1, numero2)

        self.assertEqual(resultado_esperado, resultado_obtido)



if __name__ == '__main__':
    unittest.main()
