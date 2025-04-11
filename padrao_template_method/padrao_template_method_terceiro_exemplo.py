from abc import ABCMeta, abstractmethod


class Viagem(metaclass=ABCMeta):

    @abstractmethod
    def ida(self):
        pass


    @abstractmethod
    def dia_um(self):
        pass


    @abstractmethod
    def dia_dois(self):
        pass


    @abstractmethod
    def dia_tres(self):
        pass


    @abstractmethod
    def volta(self):
        pass


    def itinerario(self): #template method 
        self.ida()
        self.dia_um()
        self.dia_dois()
        self.dia_tres()
        self.volta()


class ViagemVeneza(Viagem):
    #implementar



