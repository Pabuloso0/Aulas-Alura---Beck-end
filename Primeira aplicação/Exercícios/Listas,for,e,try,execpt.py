#1. Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lista_de_numeros:
    print(i)

# lista com quatro nomes;
lista_de_nomes = ["Pablo", "Kethully", "Aline", "João Miguel"]

# lista com ano que você nasceu e o ano atual.
lista_de_anos = [2000, 2026]

#2. Crie uma lista e ultilize um loop for para percorrer todos os elementos da lista.
lista_de_bandas = ["Beatles", "Twenty on pilots", "The Neighbourhood", "Artic Monkeys"]
print("Essas são as minhas bandas favoritas: ")
for bandas in lista_de_bandas:
    print(f".{bandas}")

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)