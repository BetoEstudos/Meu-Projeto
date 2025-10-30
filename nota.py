from disciplina import Disciplina

class Nota:
    def __init__(self, disciplina, valor):
        self.disciplina = disciplina
        self.valor = valor

    def adicionar_nota(self, Disciplina,nota):
        if nota<=3:
            Disciplina.append(nota)
        else:
            ("Você já atingiu o limite do Semestre.")