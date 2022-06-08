#'x' cria um novo arquivo
#arquivo= open("novo_arquivo.txt", 'x')

#arquivo.write('adicionei um novo arquivo')
#arquivo.close()

##Context manager
#abre o arquivo e quando sai da identação do bloco ele fecha o arquivo

with open('arquivo.txt') as arquivo:
    conteudo = arquivo.read()

conteudo += 'qualquer coisa \n'

with open('arquivo.txt', 'a') as arquivo:
    arquivo.write(conteudo)


print(conteudo)