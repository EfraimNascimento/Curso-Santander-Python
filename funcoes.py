#Definição e chamada de funções

def saudacao():
    print("Olá, mundo!")

saudacao()

#Parâmetros e argumentos

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("João")
saudacao("Maria")

#Valores de retorno

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)

#Funções anônimas (lambda)

quadrado = lambda x: x**2

print(quadrado(5))

#Escopo das variáveis (local vs. global)

def funcao():
    variavel_local = 10
    print(variavel_local)

variavel_global = 20

def funcao2():
    print(variavel_global)

funcao()
funcao2()

print(variavel_global)
print(variavel_local)

