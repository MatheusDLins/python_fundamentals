import modulo
#from modulo import pi, saudacao
import random

def soma(*args):
    soma = 0
    for num in args:
        soma += num
    return  soma

print(modulo.pi)
print(modulo.saudacao())
print(soma(1,2,3,4))
print(modulo.soma(1,2))
