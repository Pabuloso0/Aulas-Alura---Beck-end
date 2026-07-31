import subprocess
import os
from turtle import home


# ------------------------------ [Funções de exibição]-----
def exibir_nome_do_progama():
    print("Sabor express\n")

def exibir_menu():
    print("Menu de opções:\n")  
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_programa():
    exibir_subtitulo("Programa finalizado")
    

def exibir_subtitulo(Texto):
    os.system("cls" if os.name == "nt" else "clear")
    print(Texto)
    print()


# ------------------------------ [Funções de validação]-----
def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: ")
    main()

# ------------------------------ [Funções de operações]-----

restaurantes = [{"nome": "Restaurante 1", "Categoria": "Comida Japonesa", "Ativo": True}, 
                {"nome": "Restaurante 2", "Categoria": "Comida Brasileira", "Ativo": False}]

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome de restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n")

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listanto Restaurantes:")


    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["Categoria"]
        ativo = restaurante["Ativo"]
        print(f"- {nome_restaurante} / {categoria} / {ativo}")

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        print("Escolha uma opção do menu acima:\n")
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opcao_escolhida}\n")

        if opcao_escolhida == 1:
            print("Cadastrar restaurante:\n")
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print("Listar restaurantes:\n")
            listar_restaurantes()
    
        elif opcao_escolhida == 3:
            print("Ativar restaurante")
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_progama()
    exibir_menu()
    escolher_opcao()

if __name__ == "__main__":
    main()