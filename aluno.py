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
            
    def adicionar_aluno(self):
        self.carregar()
        self.aluno.append(self.to_dict())
        self.salvar()

    def salvar(self):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(self.aluno, f, indent=4, ensure_ascii=False)

    # cadastra e colocar a disciplina no dicionario
    def cadastrar_disciplina(self, displina):
        if len(displina) > 3:
            # cria uma chave com o nome da disciplina e o valor é uma lista vazia para adicionar as notas
            self.disciplinas[displina] = []

    def adicionar_nota(self, disciplina, nota, cpf):  # colocar a nota aluno
        if not self.cpf:
            if nota <= 10 and nota >= 0:
                # [disciplina] e a chave e "nota" e o valor
                self.disciplinas[disciplina].append(nota)
            else:
                print("Nota inválida. Deve ser menor ou igual a 10 e maoir que 0.")
        else:
            print("Aluno não encontrado.")

    def busca_cadastro(self, cpf, alunos):
        for aluno in alunos:
            if aluno.cpf == cpf:
                return aluno
        return None

    def calcular_media(self):
        if not self.notas:  # se o dicionario estive vazio, retuni 0
            return 0
        # "sum" soma a penas a nota por causa do "values", "len" conta a quantidade de materias pela chaves do dicionario
        return sum(self.notas.values()) / len(self.notas)

    def atualizar_nota(self, disciplina, nova_nota):
        if disciplina in self.disciplinas:  # verifica se a disciplina esta no dicionario
            if nova_nota <= 10 and nova_nota >= 0:
                self.disciplinas[disciplina] = nova_nota
        else:
            print("Disciplina não encontrada.")


# # Exemplo de uso
# aluno1 = Aluno("Welisson", "12345678900", "2023001", "Sistemas de Informação")
# aluno1.cadastrar_disciplina("Matemática")
# print(aluno1.to_dict())
# aluno1.adicionar_aluno(aluno1.to_dict())
