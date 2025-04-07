from abc import ABCMeta, abstractmethod


class Comando(metaclass=ABCMeta):
    def __init__(self, receiver):
        self.receiver = receiver 


    @abstractmethod
    def executar(self):
        pass 


class ComandoConcreto(Comando):
    def __init__(self, receiver):
        super().__init__(receiver)

    
    def executar(self):
        self.receiver.acao()


class Receiver:
    def acao(self):
        print('Ação do Receiver.')


class Invoker:
    def comando(self, comando):
        self.comando = comando


    def executar(self):
        self.comando.executar()


if __name__ == '__main__':
    receiver = Receiver()
    comando = ComandoConcreto(receiver)
    invoker = Invoker()
    invoker.comando(comando)
    invoker.executar()




    
