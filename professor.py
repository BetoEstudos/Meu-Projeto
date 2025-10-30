import os
import json
from disciplina import Disciplina

arquivo = 'professores.json'


class Professor:
    professor = []
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = []
    
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

    