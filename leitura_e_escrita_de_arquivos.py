#Leitura de arquivos

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#Escrita de arquivos

arquivo = open("dados.txt", "w")
arquivo.write("Realizando a escrita em um arquivo através do python!")
arquivo.close()

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.