#lista com o quadrado de numeros
#'normal'
def primeiros_quadrados(i):
    quadrados = []
    for num in range(i):
        quadrados.append(num*num)
    return quadrados

def primeiros_quadrados_resumido(i):
    lista_quadrados = [num*num for num in range(i)]
    return lista_quadrados

def primeiros_quadrados_pares(i):
    lista_quadrados = [num*num for num in range(i) if num % 2 == 0]
    return lista_quadrados

#lista de compra com desconto
def aplica_desconto(lista_de_compras, desconto_aplicado):
    return[(preco if preco < 100 else preco * desconto_aplicado) for preco in lista_de_compras]

precos = [88, 50, 110, 40, 150, 12.19, 123.3]
x = aplica_desconto(precos, 0.1)
print(x)