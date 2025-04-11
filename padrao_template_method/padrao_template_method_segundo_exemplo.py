from abc import ABCMeta, abstractmethod


class ClasseAbstrata(metaclass=ABCMeta):

    def __init__(self):
        pass 


    @abstractmethod
    def operacao_1(self):
        pass 


    @abstractmethod
    def operacao_2(self):
        pass 


    def template_method(self):
        print('Definindo o algoritmo: Operação 1 após Operação 2')
        self.operacao_2()
        self.operacao_1()


class ClasseConcreta(ClasseAbstrata):

    def operacao_1(self):
        print('Minha operação concreta 1')


    def operacao_2(self):
        print('Minha operação concreta 2')


class Cliente:


    def main(self):
        self.concreta = ClasseConcreta()
        self.concreta.template_method()
    

cliente = Cliente()
cliente.main()


