class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.lista_alunos = []
        self.carga_horaria = carga_horaria
        
    def add_aluno(self, aluno):
        if aluno not in self.lista_alunos:
            self.lista_alunos.append(aluno)