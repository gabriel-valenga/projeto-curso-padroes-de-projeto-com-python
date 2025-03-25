#Façade
class GerenciamentoDeEventos:

    def __init__(self):
        print('Gerenciamento de Eventos: Vou organizar com todo mundo!\n\n')

    def organizar(self):
        self.salao_de_festas = SalaoDeFestas()
        self.salao_de_festas.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.restaurante = Restaurante()
        self.restaurante.preparar_comida()

        self.banda_de_musica = BandaDeMusica()
        self.banda_de_musica.montar_palco()


#Subsistema 1
class SalaoDeFestas:
    disponivel = True 

    def __init__(self):
        print('Agendando o salão de festas')
        

    def agendar(self):
        if self.disponivel:
            print('Agendamento realizado!')
            self.disponivel = False 
        else:
            print('Salão não está disponível')


#Subsistema 2 
class Florista:

    def __init__(self):
        print('Florista: flores para um evento?')


    def arranjar_flores(self):
        print('Rosas, margaridas e lírios serão usados.\n')


#Subsistema 3
class Restaurante:

    def __init__(self):
        print('Restaurante: comida para eventos...')


    def preparar_comida(self):
        print('Comida chinesa e brasileira serão servidas.\n')


#Subsistema 4
class BandaDeMusica:

    def __init__(self):
        print('Banda: arranjos musicais para o evento...\n')


    def montar_palco(self):
        print('Preparando o palco para tocar jazz...\n')


#Cliente 
class Cliente:
    def __init__(self):
        print('Preparação para o casamento!\n')


    def contratar_gerenciamento_de_eventos(self):
        print('Vou contratar uma empresa para gerenciar o evento.\n')
        GerenciamentoDeEventos().organizar()

    
    def __del__(self):
        print('Foi muito fácil organizar esse evento!')


if __name__ == '__main__':
    Cliente().contratar_gerenciamento_de_eventos()

    
    


    