import json
import os
from aluno import Aluno
from professor import Professor

# Caminho absoluto para os arquivos de dados, relativo ao diretório deste módulo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
alunos_path = os.path.join(BASE_DIR, 'alunos.json')
professores_path = os.path.join(BASE_DIR, 'professores.json')

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
                with open(alunos_path, 'r', encoding='utf-8') as f:
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
            print("Entrando como Professor...")
            cpf_verificar = input("Digite seu CPF: ")
            senha_verificar = input("Digite sua senha: ")

            try:
                with open(professores_path, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
            except FileNotFoundError:
                print("❌ Arquivo de professores não encontrado.")
                return
            except json.JSONDecodeError:
                print("❌ Erro: arquivo de professores corrompido ou vazio.")
                return

            professores = []
            if isinstance(dados, list):
                for item in dados:
                    if isinstance(item, dict):
                        professores.append(item)
                    elif isinstance(item, list):
                        for sub in item:
                            if isinstance(sub, dict):
                                professores.append(sub)

            encontrado = False
            for prof in professores:
                if cpf_verificar == str(prof.get('cpf')) and senha_verificar == str(prof.get('senha')):
                    encontrado = True
                    print(f"\nBem-vindo(a), {prof.get('nome')}!")
                    print("\n-=-=-=- Menu Professor -=-=-=-\n")
                    print("1 - Adicionar Nota📝")
                    print("2 - Adicionar Disciplina📚")
                    print("3 - Listar Alunos👥")
                    print("4 - Listar Professores👨‍🏫")
                    print("5 - Remover Usuário❌")
                    print("6 - Editar Nota✏️")
                    print("0 - Voltar")
                    escolha_prof = input("\n----> Digite o número correspondente: ")
                    
                    if escolha_prof == "1":
                        cpf_aluno = input("Digite o CPF do aluno: ")
                        print("Digite Disciplina - Trimestre")
                        disciplina = input()
                        nota = float(input("Digite a nota: "))
                        Professor.adicionar_nota(cpf_aluno, disciplina, nota)
                    elif escolha_prof == "2":
                        # Usa o CPF do professor autenticado (cpf_verificar)
                        disciplina = input("Digite a disciplina a ser adicionada: ")
                        Professor.adicionar_disciplina(cpf_verificar, disciplina)
                    elif escolha_prof == "3":
                        # Listar alunos (visão dentro do menu do professor)
                        try:
                            with open(alunos_path, 'r', encoding='utf-8') as f:
                                dados_al = json.load(f)
                        except FileNotFoundError:
                            print("Arquivo de alunos não encontrado.")
                            break
                        except json.JSONDecodeError:
                            print("Arquivo de alunos está corrompido ou vazio.")
                            break

                        alunos_list = []
                        if isinstance(dados_al, list):
                            for item in dados_al:
                                if isinstance(item, dict):
                                    alunos_list.append(item)
                                elif isinstance(item, list):
                                    for sub in item:
                                        if isinstance(sub, dict):
                                            alunos_list.append(sub)

                        if not alunos_list:
                            print("Nenhum aluno cadastrado.")
                        else:
                            print("\n=== Lista de Alunos ===")
                            for a in alunos_list:
                                print(f"Nome: {a.get('nome')} | CPF: {a.get('cpf')} | Curso: {a.get('curso')}")
                    elif escolha_prof == "4":
                        # Listar professores (visão dentro do menu do professor)
                        try:
                            with open(professores_path, 'r', encoding='utf-8') as f:
                                dados_pr = json.load(f)
                        except FileNotFoundError:
                            print("Arquivo de professores não encontrado.")
                            break
                        except json.JSONDecodeError:
                            print("Arquivo de professores está corrompido ou vazio.")
                            break

                        professores_list = []
                        if isinstance(dados_pr, list):
                            for item in dados_pr:
                                if isinstance(item, dict):
                                    professores_list.append(item)
                                elif isinstance(item, list):
                                    for sub in item:
                                        if isinstance(sub, dict):
                                            professores_list.append(sub)

                        if not professores_list:
                            print("Nenhum professor cadastrado.")
                        else:
                            print("\n=== Lista de Professores ===")
                            for p in professores_list:
                                disc = p.get('disciplina')
                                if isinstance(disc, list):
                                    disc_repr = ", ".join(map(str, disc))
                                else:
                                    disc_repr = str(disc)
                                print(f"Nome: {p.get('nome')} | CPF: {p.get('cpf')} | Disciplina(s): {disc_repr}")
                    elif escolha_prof == "5":
                        tipo = input("Digite 'A' para aluno e 'P' para professor: ").lower()
                        cpf2 = input("Digite o CPF: ").strip()
                        if tipo == "a":
                            Aluno.remover_aluno(cpf2)
                        elif tipo == "p":
                            Professor.remover_professor(cpf2)
                    elif escolha_prof == "6":
                        # Editar nota de um aluno
                        cpf_aluno_edit = input("Digite o CPF do aluno para editar a nota: ").strip()
                        try:
                            with open(alunos_path, 'r', encoding='utf-8') as f:
                                dados_edit = json.load(f)
                        except FileNotFoundError:
                            print("Arquivo de alunos não encontrado.")
                            break
                        except json.JSONDecodeError:
                            print("Arquivo de alunos está corrompido ou vazio.")
                            break

                        # normaliza estrutura em lista simples
                        alunos_flat = []
                        if isinstance(dados_edit, list):
                            for item in dados_edit:
                                if isinstance(item, dict):
                                    alunos_flat.append(item)
                                elif isinstance(item, list):
                                    for sub in item:
                                        if isinstance(sub, dict):
                                            alunos_flat.append(sub)

                        aluno_encontrado = None
                        for a in alunos_flat:
                            if str(a.get('cpf')) == cpf_aluno_edit:
                                aluno_encontrado = a
                                break

                        if not aluno_encontrado:
                            print("Aluno não encontrado.")
                            break

                        disciplina_edit = input("Digite a disciplina cuja nota deseja editar: ").strip()
                        disciplinas = aluno_encontrado.get('disciplinas') or {}
                        if not isinstance(disciplinas, dict) or disciplina_edit not in disciplinas:
                            print("Nenhuma nota encontrada para essa disciplina.")
                            break

                        current = disciplinas.get(disciplina_edit)
                        if isinstance(current, list):
                            print("Notas atuais:")
                            for idx, val in enumerate(current, start=1):
                                print(f"{idx}. {val}")
                            escolha_idx = input("Digite o número da nota que deseja editar: ")
                            if not escolha_idx.isdigit() or int(escolha_idx) < 1 or int(escolha_idx) > len(current):
                                print("Índice inválido.")
                                break
                            novo_val = float(input("Digite a nova nota: "))
                            current[int(escolha_idx) - 1] = novo_val
                            disciplinas[disciplina_edit] = current
                        else:
                            print(f"Nota atual: {current}")
                            novo_val = float(input("Digite a nova nota: "))
                            disciplinas[disciplina_edit] = novo_val

                        aluno_encontrado['disciplinas'] = disciplinas

                        # salva de volta (gravando a lista plana)
                        try:
                            with open(alunos_path, 'w', encoding='utf-8') as f:
                                json.dump(alunos_flat, f, indent=4, ensure_ascii=False)
                            print("✅ Nota atualizada com sucesso!")
                        except Exception as e:
                            print(f"❌ Erro ao salvar arquivo de alunos: {e}")
            if not encontrado:
                print("❌ CPF ou senha incorretos.")
                return

            
        elif opcao == "0":
            return

    # Loop principal do menu
    while True:
        print("\n-=-=-=- Menu Principal -=-=-=-\n")
        print("1 - Cadastrar Aluno📝")
        print("2 - Cadastrar Professor🗒️")
        print("3 - Entrar🔐")
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
            disciplina = input("Disciplina:")
            senha=input("Senha:")
            prof = Professor(nome, cpf, senha, disciplina)
            prof.adicionar_professor()
            print("✅ Professor cadastrado com sucesso!")


        elif opcao == "3":
            entrar()

        elif opcao == "5":
            # Listar alunos
            try:
                with open(alunos_path, 'r', encoding='utf-8') as f:
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
                with open(professores_path, 'r', encoding='utf-8') as f:
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
