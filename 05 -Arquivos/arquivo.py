# Leitura

#1: abertura do arquivo
##'r' apenas leitura
arquivo = open('arquivo.txt', 'r')

#2: efetuar a leitura
#conteudo = arquivo.read()

#cria uma lista a cada \n(quebra de linha) que encontrar
conteudo = arquivo.readlines()


#Sempre que abrir o arquivo deve fechar no final
arquivo.close()


#3: apresentar conteúdo
print(conteudo)