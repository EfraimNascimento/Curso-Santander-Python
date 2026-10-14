#Entrada de dados do usuário

nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá,  " + nome + "!")
print(f"Você tem {idade} anos.")

idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Você é mair de idade.")
else:
    print("Você é menor de idade.")


#Saída de dados

nome = "Juan"
idade = 25

print(f"Olá, meno é {nome} e tenho {idade} anos.")