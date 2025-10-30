import os
import json
from disciplina import Disciplina

arquivo = 'professores.json'


class Professor:
    professor = []
    def __init__(self, disciplina, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.disciplina = []

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "senha": self.senha,
            "disciplina": self.disciplina
        }

    def lancar_nota(self, nota):
        self.aluno.adicionar_nota(self.disciplina, nota)

    def buscar_cadastro(self, cpf, professores):
        for professor in professores:
            if professor.cpf == cpf:
                return professor
        return None

    def carregar(self):
        if os.path.exists(arquivo):
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.professor.append(dados)

        else:
            self.professor = []

    def adicionar_professor(self):
        self.carregar()
        self.professor.append(self.to_dict())
        self.salvar()

    def cadastrar_disciplina(self, disciplina):
        if len(disciplina) > 3:
            self.disciplina.append(disciplina)
    
    def salvar(self):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.professor, f, indent=4, ensure_ascii=False)


# def carregar(self):
#         if os.path.exists(arquivo):
#             with open(arquivo, "r", encoding="utf-8") as f:
#                 dados = json.load(f)
#                 self.aluno.append(dados)
            
#         else:
#             self.aluno = []
            

#     def adicionar_aluno(self):
#         self.carregar()
#         self.aluno.append(self.to_dict())
#         self.salvar()

