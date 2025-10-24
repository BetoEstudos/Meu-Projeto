import json 
from aluno import Aluno
from professor import Professor

class Menu:
    def __init__(self):
        self.arquivo_dados = 'dados.json' # atributo  que guarda o nome do arquivo onde os dados serão lidos
        self.carregar_dados(self) # chama o metodo carregar dados para iniciar o menu

    def carregar_dados(self):
        # Aqui você pode adicionar a lógica para converter os dados carregados em objetos Aluno e Professor
        try:
            with open(self.arquivo_dados, "r", encoding="UTF-8") as arquivos: # ler e criar a variavel "arquivos"
                self.dados = json.load(arquivos) # parsear o conteúdo JSON do arquivo e transforma em um dicionário Python
        except FileNotFoundError: # para error na digitação do nome do arquivo
            print("Arquivo de dados não encontrado. ") # Inicia com dados vazios ou cria um novo arquivo, se necessário]
            
        opcao = input("Deseja criar um novo arquivo de dados? (s/n): ") # Pergunta ao usuário se deseja criar um novo arquivo de dados
        if opcao =="s":
            self.dados = {}
            print("Novo arquivo de dados criado.")
        else:
            print("Continuando sem criar um novo arquivo.")
            exit()

        def salvar_dados(self):
            with open(self.arquivo_dados, "w", encoding="UTF-8") as arquivos: # abrir o arquivo em modo de escrita
                json.dump(self.dados, arquivos, indent=4, ensure_ascii = False) # salvar os dados no arquivo em formato JSON