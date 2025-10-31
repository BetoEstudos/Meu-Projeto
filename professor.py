import os
import json
from aluno import Usuario

arquivo = 'professores.json'


def _flatten_list(items):
    """Retorna uma lista plana apenas com dicionários a partir de uma lista possivelmente aninhada."""
    flat = []
    if not isinstance(items, list):
        return flat
    for it in items:
        if isinstance(it, dict):
            flat.append(it)
        elif isinstance(it, list):
            # desce um nível e adiciona apenas dicts
            for sub in it:
                if isinstance(sub, dict):
                    flat.append(sub)
    return flat


class Professor(Usuario):
    professor = []
    def __init__(self, nome, cpf, disciplina=None):
        """Inicializa um Professor.

        Accepta um valor único de `disciplina` ou uma lista de disciplinas.
        """
        super().__init__(nome, cpf)
        # aceita disciplina como None, str ou lista
        if disciplina is None:
            self.disciplina = []
        elif isinstance(disciplina, list):
            self.disciplina = disciplina
        else:
            self.disciplina = [disciplina]
    
    #Transforma em dicionário
    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "disciplina": self.disciplina
        }

    # Adicionar Professor no Json
    def carregar(self):
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.professor.append(dados)

        else:
            self.professor = []
    def salvar(self):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.professor, f, indent=4, ensure_ascii=False)
    
    def adicionar_professor(self):
        self.carregar()
        self.professor.append(self.to_dict())
        self.salvar()

    @classmethod
    def adicionar_disciplina(cls, cpf, disciplina):
        """Adiciona uma disciplina a um professor identificado pelo CPF.

        Se o professor já tiver uma lista de disciplinas, adiciona; caso contrário cria a lista.
        """
        if not os.path.exists(arquivo):
            print("❌ Arquivo de professores não encontrado.")
            return

        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            print("❌ Erro: arquivo de professores corrompido ou vazio.")
            return
        except Exception as e:
            print(f"❌ Erro ao ler arquivo de professores: {e}")
            return

        profs = _flatten_list(dados) if isinstance(dados, list) else []
        cpf_str = str(cpf)
        encontrado = False
        for p in profs:
            if str(p.get('cpf')) == cpf_str:
                encontrado = True
                disc = p.get('disciplina')
                if isinstance(disc, list):
                    if disciplina not in disc:
                        disc.append(disciplina)
                elif disc:
                    # converte string para lista
                    if disciplina != disc:
                        p['disciplina'] = [disc, disciplina]
                else:
                    p['disciplina'] = [disciplina]
                break

        if not encontrado:
            print("⚠️ CPF de professor não encontrado.")
            return

        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(profs, f, indent=4, ensure_ascii=False)
            print("✅ Disciplina adicionada ao professor com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao salvar arquivo de professores: {e}")

    @classmethod
    def adicionar_nota(cls, cpf_aluno, disciplina, nota):
        """Adiciona uma nota para um aluno em uma disciplina.

        Armazena notas em `alunos.json` no campo `disciplinas` como listas de notas por disciplina.
        """
        alunos_file = 'alunos.json'
        if not os.path.exists(alunos_file):
            print("❌ Arquivo de alunos não encontrado.")
            return

        try:
            with open(alunos_file, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            print("❌ Erro: arquivo de alunos corrompido ou vazio.")
            return
        except Exception as e:
            print(f"❌ Erro ao ler arquivo de alunos: {e}")
            return

        alunos = _flatten_list(dados) if isinstance(dados, list) else []
        cpf_str = str(cpf_aluno)
        encontrado = False
        for a in alunos:
            if str(a.get('cpf')) == cpf_str:
                encontrado = True
                disc = a.get('disciplinas')
                if not isinstance(disc, dict):
                    disc = {}
                # adiciona nota na lista da disciplina
                current = disc.get(disciplina)
                if current is None:
                    disc[disciplina] = [nota]
                elif isinstance(current, list):
                    current.append(nota)
                    disc[disciplina] = current
                else:
                    disc[disciplina] = [current, nota]
                a['disciplinas'] = disc
                break

        if not encontrado:
            print("⚠️ CPF do aluno não encontrado.")
            return

        try:
            with open(alunos_file, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("✅ Nota adicionada com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao salvar arquivo de alunos: {e}")

    @classmethod
    def remover_professor(cls, cpf):
        """Remove um professor pelo CPF.

        Aceita CPF como string ou número e lida com listas aninhadas no JSON.
        """
        # verifica existência do arquivo
        if not os.path.exists(arquivo):
            print("❌ Arquivo de professores não encontrado.")
            return

        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            print("❌ Erro: arquivo JSON corrompido ou vazio.")
            return
        except Exception as e:
            print(f"❌ Erro ao ler arquivo: {e}")
            return

        professores = _flatten_list(dados) if isinstance(dados, list) else []

        if not professores:
            print("❌ Nenhum professor cadastrado.")
            return

        cpf_str = str(cpf)
        novos = [p for p in professores if str(p.get('cpf')) != cpf_str]

        if len(novos) == len(professores):
            print("⚠️ CPF não encontrado, nenhum professor removido.")
            return

        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(novos, f, indent=4, ensure_ascii=False)
            print("✅ Professor removido com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao salvar arquivo: {e}")