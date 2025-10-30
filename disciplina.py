class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.lista_alunos = []
        
    def add_aluno(self, aluno):
        if aluno not in self.lista_alunos:
            self.lista_alunos.append(aluno)