from aluno import Aluno # "Tradução"- do arquivo aluno importe "Aluno" --> que e uma classe  
from disciplina import Disciplina

class Professor:
    def __init__(self,disciplina,nome,cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.disciplina = []
    
    def lancar_nota(self, nota):
        self.aluno.adicionar_nota(self.disciplina, nota)

    def buscar_cadastro(self, cpf, professores):
        for professor in professores:
            if professor.cpf == cpf:
                return professor
        return None
    
    def cadastrar_disciplina(self, disciplina):
        if len(disciplina) > 3:
            self.disciplina.append(disciplina)  