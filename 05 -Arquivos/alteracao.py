with open('cadastro.csv', 'r') as arquivo:
    cadastro = arquivo.readlines()


def cadastrar():
    cpf = input('CPF: ')
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input('Sexo: ')
    uf = input('UF: ')

    registro = f'{cpf},{nome},{idade},{sexo},{uf}\n'

    with open('cadastro.csv', 'a') as arquivo:
        arquivo.writelines(registro)

def modificar():
    cpf = '33333'

    for indice in range(len(cadastro)):
        if cadastro[indice].split(',')[0] == cpf:
            cpf = input('CPF: ')
            nome = input("Nome: ")
            idade = input("Idade: ")
            sexo = input('Sexo: ')
            uf = input('UF: ')

            cadastro[indice] = f'{cpf},{nome},{idade},{sexo},{uf}\n'

            with open('cadastro.csv', 'w') as arquivo:
                arquivo.writelines(cadastro)

def deletar():
    cpf = '33333'

    for indice in range(len(cadastro)):
        if cadastro[indice].split(',')[0] == cpf:
            print(cadastro[indice])
            del cadastro[indice]
            break

    with open('cadastro.csv', 'w') as arquivo:
        arquivo.writelines(cadastro)