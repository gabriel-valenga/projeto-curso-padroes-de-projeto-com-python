from db import _executar


class Produto:

    def __init__(self, nome, preco, id = None):
        self.id = id 
        self.nome = nome
        self.preco = preco 
        self.status = 1 # 1 - ativo / 0 - inativo 
        
        #se a tabela prduto nao existir, crie-a
        query = """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            , nome TEXT
            , preco REAL
            , status NUMERIC
        )
        """
        _executar(query)
        
