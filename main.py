from aluno import Aluno
from professor import Professor
import os


def menu():
    def entra():
        print("--------------ENTRAR--------------")
        print("1- Aluno")
        print("2- Professor")
        print("0- Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Entrando como Aluno...")
        elif opcao == "2":
            print("Entrando como Professor...")
        elif opcao == "0":
            print("Saindo...")
            menu()
    while True:
        print("\n-=-=-=- Menu Principal -=-=-=-\n")
        print("1 - Cadatrar Aluno📝")
        print("2 - Cadatrar Professor🗒️")
        print("3 - Entra")
        print("0 - Sair")
        opcao = input("\n----> Digite o número correspondente:")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = int(input("Cpf: "))
            matricula = float(input("Matricula: "))
            curso = input("Curso: ")
            aluno = Aluno(nome, cpf, matricula, curso)
            aluno.adicionar_aluno()
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Nome: ")
            cpf = int(input("Cpf: "))
            disciplina = float(input("Matricula: "))
            senha = input("Curso: ")
            professor = Professor(nome, cpf, senha, disciplina)
            professor.adicionar_professor()
            print("Professor cadastrado com sucesso!")

        elif opcao == "3":
            entra()

        elif opcao == "0":
            print("Saindo...")
            os.system("cls")
            break
        else:
            print("Opção inválida!")
            os.system("cls")

if __name__ == "__main__":
    menu()
