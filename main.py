import json
import os
from aluno import Aluno
from professor import Professor


def menu():
    def entrar():
        print("--------------ENTRAR--------------")
        print("1- Aluno")
        print("2- Professor")
        print("0- Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Entrando como Aluno...")
            cpf = input("Digite seu CPF: ")

            try:
                with open('alunos.json', 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            except FileNotFoundError:
                print("Arquivo de alunos não encontrado.")
                return

            encontrado = False
            for aluno_data in dados:
                if cpf == str(aluno_data['cpf']):
                    encontrado = True
                    print("\n=== Dados do aluno ===")
                    print(f"Nome: {aluno_data['nome']}")
                    print(f"CPF: {aluno_data['cpf']}")
                    print(f"Curso: {aluno_data['curso']}")
                    print("mostrar nota")
                    

            if not encontrado:
                print("❌ Aluno não encontrado.")

        elif opcao == "2":
            print("\n-=-=-=- Menu Professor -=-=-=-\n")
            print("1 - Adicionar Nota📝")
            print("2 - Adicionar Disciplina📚")
            print("0 - Voltar")
            escolha_prof = input("\n----> Digite o número correspondente: ")

            if escolha_prof == "1":
                cpf_aluno = input("Digite o CPF do aluno: ")
                disciplina = input("Digite a disciplina: ")
                nota = float(input("Digite a nota: "))
                Professor.adicionar_nota(cpf_aluno, disciplina, nota)

        elif opcao == "0":
            return

    # Loop principal do menu
    while True:
        print("\n-=-=-=- Menu Principal -=-=-=-\n")
        print("1 - Cadastrar Aluno📝")
        print("2 - Cadastrar Professor🗒️")
        print("3 - Remover Usuário❌")
        print("4 - Entrar🔐")
        print("0 - Sair🚪")
        opcao = input("\n----> Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            aluno_obj = Aluno(nome, cpf, matricula, curso)
            aluno_obj.adicionar_aluno()
            print("✅ Aluno cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            disciplina = input("Disciplina: ")
            prof = Professor(nome, cpf, disciplina)
            prof.adicionar_professor()
            print("✅ Professor cadastrado com sucesso!")

        elif opcao == "3":
            tipo = input("Digite 'A' para aluno e 'P' para professor: ").lower()
            cpf2 = input("Digite o CPF: ").strip()

            if tipo == "a":
                Aluno.remover_aluno(cpf2)
            elif tipo == "p":
                Professor.remover_professor(cpf2)
            else:
                print("Tipo inválido!")

        elif opcao == "4":
            entrar()

        elif opcao == "0":
            print("Saindo...")
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    menu()