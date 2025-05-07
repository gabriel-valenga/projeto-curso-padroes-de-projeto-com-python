from abc import ABCMeta


class EstadoComputador(metaclass=ABCMeta):
    nome = "EstadoComputador"
    permitido = []


    def mudar(self, estado):
        if estado.nome in self.permitido:
            print(f'Atual: {self} => mudado para {estado.nome}')
            self.__class__ = estado
        else:
            print(f'Atual: {self} => não é possível mudar para {estado.nome}')

    
    def __str__(self):
        return self.nome
    

class Ligar(EstadoComputador):
    nome = "Ligar"
    permitido = ["Desligar", "Suspender", "Hibernar"]


class Desligar(EstadoComputador):
    nome = "Desligar"
    permitido = ["Ligar"]


class Suspender(EstadoComputador):
    nome = "Suspender"
    permitido = ["Ligar"]


class Hibernar(EstadoComputador):
    nome = "Hibernar"
    permitido = ["Ligar"]


class Computador():

    def __init__(self, marca = "Dell"):
        self.marca = marca 
        self.estado = Desligar()

    
    def alterar_estado(self, estado):
        self.estado.mudar(estado)


if __name__ == '__main__':
    computador = Computador()
    computador.alterar_estado(Ligar)
    computador.alterar_estado(Desligar)
    computador.alterar_estado(Suspender)
    computador.alterar_estado(Ligar)
    computador.alterar_estado(Suspender)
    computador.alterar_estado(Hibernar)
    computador.alterar_estado(Ligar)
    computador.alterar_estado(Hibernar)
    computador.alterar_estado(Ligar)
    computador.alterar_estado(Desligar)









        
