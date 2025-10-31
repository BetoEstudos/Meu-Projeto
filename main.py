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
            # Normaliza dados (aplana listas aninhadas de nível 1)
            alunos = []
            if isinstance(dados, list):
                for item in dados:
                    if isinstance(item, dict):
                        alunos.append(item)
                    elif isinstance(item, list):
                        for sub in item:
                            if isinstance(sub, dict):
                                alunos.append(sub)

            encontrado = False
            for aluno_data in alunos:
                if cpf == str(aluno_data.get('cpf')):
                    encontrado = True
                    print("\n=== Dados do aluno ===")
                    print(f"Nome: {aluno_data.get('nome')}")
                    print(f"CPF: {aluno_data.get('cpf')}")
                    print(f"Curso: {aluno_data.get('curso')}")

                    # Mostrar notas por disciplina
                    disciplinas = aluno_data.get('disciplinas') or {}
                    if isinstance(disciplinas, dict) and disciplinas:
                        print("\n--- Notas ---")
                        for disc, notas in disciplinas.items():
                            if isinstance(notas, list):
                                notas_repr = ", ".join(map(str, notas))
                            else:
                                notas_repr = str(notas)
                            print(f"{disc}: {notas_repr}")
                    else:
                        print("Nenhuma nota cadastrada.")
                    break

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
            elif escolha_prof == "2":
                cpf_prof = input("Digite o CPF do professor: ")
                disciplina = input("Digite a disciplina a ser adicionada: ")
                Professor.adicionar_disciplina(cpf_prof, disciplina)

        elif opcao == "0":
            return

    # Loop principal do menu
    while True:
        print("\n-=-=-=- Menu Principal -=-=-=-\n")
        print("1 - Cadastrar Aluno📝")
        print("2 - Cadastrar Professor🗒️")
        print("3 - Remover Usuário❌")
        print("4 - Entrar🔐")
        print("5 - Listar Alunos👥")
        print("6 - Listar Professores👨‍🏫")
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
            tipo = input(
                "Digite 'A' para aluno e 'P' para professor: ").lower()
            cpf2 = input("Digite o CPF: ").strip()

            if tipo == "a":
                Aluno.remover_aluno(cpf2)
            elif tipo == "p":
                Professor.remover_professor(cpf2)
            else:
                print("Tipo inválido!")

        elif opcao == "4":
            entrar()

        elif opcao == "5":
            # Listar alunos
            try:
                with open('alunos.json', 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            except FileNotFoundError:
                print("Arquivo de alunos não encontrado.")
                continue
            except json.JSONDecodeError:
                print("Arquivo de alunos está corrompido ou vazio.")
                continue

            # Normaliza estrutura (aplana listas aninhadas de nível 1)
            alunos = []
            if isinstance(dados, list):
                for item in dados:
                    if isinstance(item, dict):
                        alunos.append(item)
                    elif isinstance(item, list):
                        for sub in item:
                            if isinstance(sub, dict):
                                alunos.append(sub)

            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                print("\n=== Lista de Alunos ===")
                for a in alunos:
                    print(f"Nome: {a.get('nome')} | CPF: {a.get('cpf')} | Curso: {a.get('curso')}")

        elif opcao == "6":
            # Listar professores
            try:
                with open('professores.json', 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            except FileNotFoundError:
                print("Arquivo de professores não encontrado.")
                continue
            except json.JSONDecodeError:
                print("Arquivo de professores está corrompido ou vazio.")
                continue

            professores = []
            if isinstance(dados, list):
                for item in dados:
                    if isinstance(item, dict):
                        professores.append(item)
                    elif isinstance(item, list):
                        for sub in item:
                            if isinstance(sub, dict):
                                professores.append(sub)

            if not professores:
                print("Nenhum professor cadastrado.")
            else:
                print("\n=== Lista de Professores ===")
                for p in professores:
                    disc = p.get('disciplina')
                    if isinstance(disc, list):
                        disc_repr = ", ".join(map(str, disc))
                    else:
                        disc_repr = str(disc)
                    print(f"Nome: {p.get('nome')} | CPF: {p.get('cpf')} | Disciplina(s): {disc_repr}")

        elif opcao == "0":
            print("Saindo...")
            os.system("cls" if os.name == "nt" else "clear")
            break
        else:
            print("❌ Opção inválida!")
            menu()


if __name__ == "__main__":
    menu()
