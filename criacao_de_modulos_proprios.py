#Criar e utilizar módulos personalizados

#meu_modulo.py

def saudar(nome):
    print(f"Olá, {nome}!")

def calcular_soma(a, b):
    return a + b

#Em outro arquivo:

# meu_modulo.saudar("João") #meu_modulo sendo o nome do arquivo
# resultado =  meu_modulo.calcular_soma(5, 3)
# print(resultado)

#Organização do código em módulos

#operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

#utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)

def obter_nome_usuario():
    return input("Digite seu nome: ")

#Em outro arquivo:

# import operacoes
# import utilidades

# resultado = operacoes.somar(5, 3)
# utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

# nome = utilidades.obter_nome_usuario()
# utilidades.imprimir_mensagem(f"Olá, {nome}!")

