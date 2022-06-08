import unittest
from ecommerce import Produto, CarrinhoDeCompra

class TesteEcommerce(unittest.TestCase):
    def setUp(self):
        self.p1 = Produto("Camiseta", 9.90)
        self.p2 = Produto("Calça Jeans", 10.90)
        self.c1 = CarrinhoDeCompra()

    def adiciona_produtos_no_carrinho(self):
        self.c1.adicionaProduto(self.p1)
        self.c1.adicionaProduto(self.p2)

    def calcula_total_de_compras(self):
        self.total_de_compras = self.c1.calculaTotalDeCompras()

    def make_assertions(self):
        self.assertEqual(2, len(self.c1.carrinho))
        self.assertEqual(self.p1.preco + self.p2.preco, self.total_de_compras)

    def teste_ecommerce(self):
        self.adiciona_produtos_no_carrinho()
        self.calcula_total_de_compras()
        self.make_assertions()
        