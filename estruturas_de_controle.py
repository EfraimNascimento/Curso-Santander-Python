#IF

# if condicao: 
#     Bloco de código a executar se a condição for verdadeira

idade = 18

if idade >= 18:
    print("Você é maior de idade.")

#IF-ELSE

idade = 15

if idade >= 18:
    print("Você é maior de idade.")
else: 
    print("Você é menor de idade.")

#IF-ELIF-ELSE

# if condicao1:

#    # Bloco de código a executar se a condicao1 for verdadeira
#    instruções

# elif condicao2:

#    # Bloco de código a executar se a condicao2 for verdadeira
#    instruções

# else:

#    # Bloco de código a executar se nenhuma condição anterior for verdadeira
#    instruções

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muito bom")
elif nota >= 70:
    print("Bom")
else:
    print("Precisa melhorar")

