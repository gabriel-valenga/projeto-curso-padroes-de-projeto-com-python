from abc import ABCMeta, abstractmethod


#Interface
class Carteira(metaclass=ABCMeta):
    @abstractmethod
    def pagar(self):
        pass


#Objeto real
class Banco(Carteira):

    def __init__(self):
        self.numero_cartao = None 
        self.numero_conta = None 


    def __get_conta(self):
        self.numero_conta = self.numero_cartao
        return self.numero_conta
    

    def __tem_saldo(self):
        print(f'Banco:: Checando se a conta f{self.__get_conta()} tem saldo...')
        return True
    

    def set_numero_cartao(self, numero_cartao):
        self.numero_cartao = numero_cartao


    def pagar(self): #implementando metodo da Interface Carteira
       if self.__tem_saldo():
           print('Banco:: Pagando a conta...')
           return True 
       else:
           print('Banco:: Desculpe você não tem saldo suficiente.')
           return False
       

#Proxy
class CartaoDebito(Carteira):
    def __init__(self):
        self.banco = Banco()


    def pagar(self):
        numero_do_cartao = input('Proxy:: Insira o número do cartão:')
        self.banco.set_numero_cartao(numero_do_cartao)
        return self.banco.pagar()
    

#Cliente
class Cliente:
    def __init__(self):
        print('Cliente:: Quero comprar uma cerveja')
        self.cartao_de_debito = CartaoDebito()
        self.comprei = None


    def fazer_pagamento(self):
        self.comprei = self.cartao_de_debito.pagar()


    def __del__(self):
        if self.comprei:
            print('Cliente:: Finalmente vou tomar uma cerveja!')
        else:
            print('Cliente:: Gostaria de ter mais dinheiro...')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.fazer_pagamento()