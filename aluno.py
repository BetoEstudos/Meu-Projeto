import json 
from arquivo import Arquivo
from arquivo import _arquivo

class Aluno(Arquivo):
    def __init__(self,nome,cpf, matricula, curso):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.curso = curso
        self.disciplinas = {} # Dicionário para lista as notas
        self.salvar(self.to_dict())
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "matricula": self.matricula,
            "curso": self.curso,
            "disciplinas": self.disciplinas
        }
        
    
    def cadastrar_disciplina(self,displina):# cadastra e colocar a disciplina no dicionario
        if len(displina) > 3:
            self.disciplinas[displina] = []
        
        

    def adicionar_nota(self, disciplina, nota,cpf): # colocar a nota aluno
        if not self.cpf:
            if nota <= 10 and nota >= 0:
                self.disciplinas[disciplina].append(nota)# [disciplina] e a chave e "nota" e o valor
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
        if not self.notas: # se o dicionario estive vazio, retuni 0
            return 0 
        return sum(self.notas.values())/ len(self.notas) # "sum" soma a penas a nota por causa do "values", "len" conta a quantidade de materias pela chaves do dicionario
    
    def atualizar_nota(self, disciplina, nova_nota):
        if disciplina in self.disciplinas: # verifica se a disciplina esta no dicionario
            if nova_nota <= 10 and nova_nota >= 0:
                self.disciplinas[disciplina] = nova_nota
        else:
            print("Disciplina não encontrada.")
            
# Exemplo de uso
            
aluno1 = Aluno("Welisson","12345678900","2023001","Sistemas de Informação")
aluno1.cadastrar_disciplina("Matemática")
print(aluno1.to_dict())