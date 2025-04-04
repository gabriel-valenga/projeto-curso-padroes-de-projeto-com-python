class Instalador:
    def __init__(self, fonte, destino):
        self.opcoes = []
        self.destino = destino 
        self.fonte = fonte


    def preferencias(self, escolha):
        self.opcoes.append(escolha)


    def executar(self):
        for opcao in self.opcoes:
            if list(opcao.values())[0]:
                print(f'Copiando os binários de {self.fonte} para {self.destino}')
            else:
                print('Operação finalizada')


if __name__ == '__main__':
    #inicia o instalador 
    instalador = Instalador('python 3.12.9.gzip', '/usr/bin/')

    #o usuario escolhe instalar apenas o python
    instalador.preferencias({'python': True})
    instalador.preferencias({'java': False})

    #Executa a instalação
    instalador.executar()

