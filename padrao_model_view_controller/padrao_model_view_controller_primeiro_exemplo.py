
class Modelo:

    def __init__(self):
        self.produtos = {
            'ps5': {'id': 1, 'nome': 'Playstation 5', 'preco': '4000'},
            'xbox_sx': {'id': 2, 'nome': 'XBOX Series X', 'preco': '4000'},
            'nintendo_switch': {'id': 3, 'nome': 'Nintendo Switch', 'preco': '2000'}
        }


class Controlador:

    def __init__(self):
        self.modelo = Modelo()


    def listar_produtos(self):
        chaves_produtos = self.modelo.produtos.keys()
        print('---------Produtos---------')
        for chave_produto in chaves_produtos:
            print(f"ID: {self.modelo.produtos[chave_produto]['id']}")
            print(f"NOME: {self.modelo.produtos[chave_produto]['nome']}")
            print(f"PREÇO: {self.modelo.produtos[chave_produto]['preco']}\n")


class Visao:

    def __init__(self):
        self.controlador = Controlador()


    def produtos(self):
        self.controlador.listar_produtos()



if __name__ == '__main__':
    visao = Visao()
    visao.produtos()
    
