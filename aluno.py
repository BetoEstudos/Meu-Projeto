class Aluno:
    def __init__(self,nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.notas = {} # Dicionário para lista as notas

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota # [disciplina] e a chave e "nota" e o valor

    def calcular_media(self):
        if not self.notas: # se o dicionario estive vazio
            return 0 
        return sum(self.notas.values())/ len(self.notas) # "sum" soma a penas a nota por causa do "values", "len" conta a quantidade de materias pela chaves do dicionario