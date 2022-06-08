dic = {
    '1': lambda x,y : x + y,
    '2': lambda x,y : x - y,
    '3': lambda x,y : x * y,
    '4': lambda x,y : x / y,
    '5': lambda x,y : exit()
}

while True:

    try: #bloco com potencial travamento (chance de erro acontecer)
        n1 = float(input('N1: '))
        n2 = float(input('N2: '))
        

        op = input(f'Digite a opção desejada \n' \
            f'1 - Soma \n' \
            f'2 - Subtração \n' \
            f'3 - Multiplicação \n' \
            f'4 - Divisão \n' \
            f'5 - Sair \n')

        res = dic[op](n1,n2)

    except ZeroDivisionError:
        print("Não pode ser dividido por zero")
    
    except KeyError:
        print("Digite uma opção válida")

    except ValueError:
        print("Digite apenas números")

    except Exception as err:
        print("erro desconhecido", err)

    else:
        #caso a instrução for bem sucedida
        print(res)

    #sempre executa depois do try
    finally:
        print("passei aqui")