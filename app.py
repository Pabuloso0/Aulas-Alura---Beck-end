import subprocess
import os
from turtle import home

def exibir_nome_do_progama():
    print("Sabor express\n")

def exibir_menu():
    print("Menu de opções:\n")  
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_programa():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Programa finalizado.\n")

def escolher_opcao():
    print("Escolha uma opção do menu acima:\n")
    opcao_escolhida = int(input("Escolha uma opção: "))
    print(f"Você escolheu a opção {opcao_escolhida}\n")

    if opcao_escolhida == 1:
        print("Cadastrar restaurante")
    elif opcao_escolhida == 2:
        print("Listar restaurantes")
    elif opcao_escolhida == 3:
        print("Ativar restaurante")
    else:
        finalizar_programa()

def main():
    exibir_nome_do_progama()
    exibir_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()