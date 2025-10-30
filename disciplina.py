class Disciplina:
<<<<<<< HEAD
    def __init__(self, nome):
        self.nome = nome
        self.lista_alunos = []
=======

    def __init__(self, aluno, nome, nota):
        self.aluno = aluno
        self.nome = nome
        self.nota = nota
>>>>>>> 421d6649c8b6b8e5aa1606ebfbe883186f374e03
        
        
    def to_dict(self):
        return {
            "aluno": self.aluno,
            "nome": self.nome,
            "nota": self.nota
        }
    
    # def add_aluno(self, aluno):
    #     if aluno not in self.lista_alunos:
    #         self.lista_alunos.append(aluno)

    def adicionar_nota(self, disciplina, nota, cpf):  # colocar a nota aluno
        if not self.cpf:
            if nota <= 10 and nota >= 0:
                # [disciplina] e a chave e "nota" e o valor
                self.disciplinas[disciplina].append(nota)
            else:
                print("Nota inválida. Deve ser menor ou igual a 10 e maoir que 0.")
        else:
            print("Aluno não encontrado.")
