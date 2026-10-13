#Criação e operações básicas

frutas = {
    "Maçâ",
    "Banana",
    "Laranja"
}

numeros = set([1, 2, 3, 4, 5])

#Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  


intersecao = conjunto1 & conjunto2
print(intersecao) 


diferenca = conjunto1 - conjunto2
print(diferenca)  


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  

# add(elemento): adiciona um elemento ao conjunto.
# remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
# discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
# clear(): remove todos os elementos do conjunto.

frutas.add("Pera")
print(frutas)

frutas.remove("Banana")
print(frutas)

frutas.discard("Uva")
print(frutas)

frutas.clear()
print(frutas)
