import json
import os

arquivo = "alunos.json"


def _flatten_list(data):
    """Flatten nested lists one level deep and keep only dict items."""
    if not isinstance(data, list):
        return []
    result = []
    for item in data:
        if isinstance(item, list):
            for sub in item:
                if isinstance(sub, dict):
                    result.append(sub)
        elif isinstance(item, dict):
            result.append(item)
    return result
class Usuario:
    def __init__(self, nome, cpf, senha=None):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

class Aluno(Usuario):
    aluno = []

    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = {}  # Dicionário para lista as notas

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "matricula": self.matricula,
            "curso": self.curso,
            "disciplinas": self.disciplinas,
        }

    # Adicionar Aluno ao Json
    def carregar(self):
        """
        Carrega alunos do arquivo e normaliza a estrutura.
        Garante que `self.aluno` seja sempre uma lista simples de dicionários.
        """
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []

            # Normaliza estrutura (remove listas aninhadas)
            if isinstance(dados, list):
                self.aluno = _flatten_list(dados)
            else:
                self.aluno = []
        else:
            self.aluno = []

    def salvar(self):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.aluno, f, indent=4, ensure_ascii=False)

    def adicionar_aluno(self):
        self.carregar()
        self.aluno.append(self.to_dict())
        self.salvar()

    # Remover Aluno
    @classmethod
    def remover_aluno(cls, cpf):
        try:
            if os.path.exists(arquivo):
                with open(arquivo, "r", encoding="utf-8") as f:
                    dados = json.load(f)
            else:
                print("❌ Arquivo de alunos não encontrado.")
                return

            alunos = _flatten_list(dados) if isinstance(dados, list) else []

            novos = [a for a in alunos if str(a.get('cpf')) != str(cpf)]

            if len(novos) == len(alunos):
                print("⚠️ CPF não encontrado, nenhum aluno removido.")
                return

            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump(novos, f, indent=4, ensure_ascii=False)

            print("✅ Aluno removido com sucesso!")
        except json.JSONDecodeError:
            print("❌ Erro: arquivo JSON corrompido ou vazio.")
        except Exception as e:
            print(f"❌ Erro ao remover aluno: {e}")
