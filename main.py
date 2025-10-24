import json
import professor
import aluno 


class Menu:
    def __init__(self, nome, cargo, senha):
        self.nome = nome
        self.cargo = cargo
        self.__senha = senha

    def menu(self):
        self.nome = input("Digite o Nome do Usuario")
        self.cargo = input("Digite o cargo, ex('Professor, Aluno')")
        self.__senha = int(input("Digite a senha"))
        lista = [self.nome, self.cargo,]

    def lista(self, lista):
        print(lista)


if __name__ == "__main__":
    Menu()
