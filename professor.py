from aluno import Aluno # "Tradução"- do arquivo aluno importe "Aluno" --> que e uma classe  

class Professor:
    def __init__(self,disciplina,nome):
        self.nome = nome
        self.disciplina = disciplina
    
    def lancar_nota(self,discilpina, nota):
        Aluno.adicionar_nota(self.disciplina, nota)