#Listas

frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

#índices negativos

print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

# append(elemento): adiciona um elemento ao final da lista.
# insert(indice, elemento): insere um elemento em uma posição específica da lista.
# remove(elemento): remove a primeira ocorrência de um elemento na lista.
# pop(indice): remove e retorna o elemento em uma posição específica da lista.
# sort(): ordena os elementos da lista em ordem ascendente.
# reverse(): inverte a ordem dos elementos na lista.

frutas.append("pera")
print(frutas)

frutas.insert(1, "uva")
print(frutas)

frutas.remove("banana")
print(frutas)

fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

#Listas de compreensão

# nova_lista = [expressão for elemento in sequência if condição]

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)