from abc import ABCMeta, abstractmethod


#command
class Ordem(metaclass=ABCMeta):
    @abstractmethod
    def executar(self):
        pass 


#comando concreto
class OrdemCompra(Ordem):
    def __init__(self, acao):
        self.acao = acao


    def executar(self):
        self.acao.comprar()


#comando concreto
class OrdemVenda(Ordem):
    def __init__(self, acao):
        self.acao = acao


    def executar(self):
        self.acao.vender()

#Receiver
class Acao:
    def comprar(self):
        print('Você irá comprar ações...')


    def vender(self):
        print('Você irá vender ações...')
         
#Invoker
class Agente:
    def __init__(self):
        self.__fila_ordens = []


    def adicionar_ordem_na_fila(self, ordem):
        self.__fila_ordens.append(ordem)


    def executar_ordens(self):
        for ordem in self.__fila_ordens:
            ordem.executar()


if __name__ == '__main__':
    #Cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)
    #Chamador/Invoker
    agente = Agente()
    agente.adicionar_ordem_na_fila(ordem_compra)
    agente.adicionar_ordem_na_fila(ordem_venda)
    agente.executar_ordens()

