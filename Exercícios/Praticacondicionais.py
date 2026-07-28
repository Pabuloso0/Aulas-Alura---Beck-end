# Hora da prática: Condicionais

# Exercícios:

# 1. Solicite ao usuário que digite um número inteiro e verifique se ele é par ou ímpar. 
# Imprima uma mensagem informando o resultado.

numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.\n")
else:
    print(f"O número {numero} é ímpar.\n")

# 2. Pergunte ao usuário a sua idade e verifique se ele é maior de idade (18 anos ou mais).
# classifique se ele é criança, adolescente ou adulto e imprima uma mensagem correspondente.
# criança: 0-12 anos, adolescente: 13-18 anos, adulto: 18 anos ou mais.

idade = int(input("Digite sua idade: ")) 

if 0 < idade < 12:
    print("Você é criança\n")
elif 13 <= idade <= 18:
    print("Você é adolescente")
else:
    print("Você é adulto ou mais\n")

#3. Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha 
# fornecidos correspondem aos valores esperados determinados por você.

usuario_correto = "Pabuloso_0"
senha_correta = "pablo123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite sua senha:")

if usuario_correto == usuario and senha == senha_correta:
    print("Login bem sucedido\n")
else:
    print("Credenciais inválidas. Tente novamente mais tarde")

#4 - Solicite ao usuário as coordenas (x, y) de um ponto qualquer e utilize uma estrutura if elif else
# para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes
# condições:

# - Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# - Segundo Quadrante: O valor de x é menor que zero e o valor de y é maior que zero.
# - Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# - Quarto Quadrante: O valor de x é maior que zero e y é menor que zero;
# - Caso contrário: O ponto está localizando no eixo ou origem.

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.") 
