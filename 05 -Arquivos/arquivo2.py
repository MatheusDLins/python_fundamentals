##'w' escrever do zero o arquivo
#abrir o conteúdo e salvar em uma variável
arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.readlines()
arquivo.close()

conteudo.append("\nNova linha de exemplo")
arquivo= open("arquivo.txt", 'w')

arquivo.writelines(conteudo)
arquivo.close()