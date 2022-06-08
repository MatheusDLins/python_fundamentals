from random import randint
import unittest
import calculadora

#executar o comando "python -m unittest teste_calculadora.py" no terminal para verificar os testes

class TesteCalculadora(unittest.TestCase):
    def test_soma(self):
        n1 = randint(0,999)
        n2 = randint(0,999)
        soma = n1 + n2
        self.assertEquals(soma, calculadora.soma(n1,n2))

    def test_divisao_esperada(self):
        n1 = randint(0,999)
        n2 = randint(1,999)
        div = n1 / n2
        self.assertEquals(div, calculadora.divisao(n1,n2))

    def test_divisao_por_zero(self):
        n1 = randint(0,999)
        n2 = 0
        div_zero = "Não pode dividir por zero"
        self.assertEquals(div_zero, calculadora.divisao(n1,n2))