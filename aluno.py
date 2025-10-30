import json
import os
from arquivo import Arquivo
arquivo = 'alunos.json'


class Aluno(Arquivo):
    aluno = []
    def __init__(self, nome, cpf, matricula, curso):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = {}  # Dicionário para lista as notas

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "matricula": self.matricula,
            "curso": self.curso,
            "disciplinas": self.disciplinas
        }
    
    # Adicionar Aluno ao Json
    def carregar(self):
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.aluno.append(dados)
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
    def remover_aluno(self, cpf2):
        for a in self.aluno:
            if a["cpf"] == cpf2:
                self.aluno.remove(a)
        self.salvar()
