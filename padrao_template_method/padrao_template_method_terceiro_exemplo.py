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
    
    def ida(self):
        print('Viagem de avião até Veneza...')


    def dia_um(self):
        print('Visita a basílica de São Marcos na Praça de São Marcos')


    def dia_dois(self):
        print('Visita ao Palácio Doge')


    def dia_tres(self):
        print('Aproveitar a comida próximo a Ponte Rialto')

    
    def volta(self):
        print('Viagem de avião de Veneza até o Brasil...')


class ViagemMalvinas(Viagem):
    
    def ida(self):
        print('Viagem de ônibus até a Argentina de depos de barco até as ilhas...')


    def dia_um(self):
        print('Apreciar a vida marinha.')


    def dia_dois(self):
        print('Visita a cidade de Stanley.')


    def dia_tres(self):
        print('Relaxar e se preparar para a viagem de volta.')

    
    def volta(self):
        print('Viagem de barco até a Argentina e depois de ônibus até o Brasil...')


class GeekTravel:

    def preparar_viagem(self):
        opcao = input('Qual viagem deseja fazer? [Veneza, Malvinas]')
        if opcao == 'Veneza':
            self.viagem = ViagemVeneza()
        elif opcao == 'Malvinas':
            self.viagem = ViagemMalvinas()
        else:
            print('Essa viagem não está disponível.')
            return
        self.viagem.itinerario()


agencia = GeekTravel()
agencia.preparar_viagem()


