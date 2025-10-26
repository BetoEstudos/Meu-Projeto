import json

class Arquivo:
    _arquivo = 'name.json'

    @classmethod
    def carregar(cls):
        with open(cls._arquivo, "r", encoding="UTF-8") as arquivo:
            dado = json.load(arquivo)
            return dado
        return False

    @classmethod
    def salvar(cls, dado):
        with open(cls._arquivo, "w", encoding="UTF-8") as arquivo:
            json.dump(dado, arquivo, indent=4, ensure_ascii=False)
            return True
        return False