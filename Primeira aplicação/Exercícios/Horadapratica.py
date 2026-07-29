# Exercícios

# 1. imprima a frase "python na escola de progamação alura:
print("Python na escola de progamação Alura")

# 2. imprima a frase: Meu nome é {seu nome} e tenho {sua idade} anos em que o nome e 
# idade são variáveis que você deve criar e atribuir valores a elas."

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

print(f"Meu nome é {nome} e tenho {idade} anos.")

# 3. imprima a Palavra "Alura"  de forma que cada letra fique em uma linha, como mostrado abaixo:
# A
# L
# U
# R 
# A

print("A", "L", "U", "R", "A", sep="\n")

# 4. imprima a frase: O valor redondo de pi é: {valor de pi arredondado para 2 casas decimais} 
# em que o valor de pi deve ser obtido da biblioteca math e arredondado para 2 casas decimais.

import math
pi= math.pi
print(f"O valor redondo de pi é: {round(pi, 2)}")
