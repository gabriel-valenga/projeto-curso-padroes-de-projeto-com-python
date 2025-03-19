class Servidor:
    def __init__(self, nome:str):
        self.nome = nome


    def __str__(self):
        return self.nome


class SanidadeCheck:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not SanidadeCheck.__instance:
            SanidadeCheck.__instance = super(SanidadeCheck, cls).__new__(cls, *args, **kwargs)
        return SanidadeCheck.__instance
    

    def __init__(self):
        self.__servidores = []


    def checar_servidor(self, servidor_a_ser_checado:Servidor):
        indice_servidor = next((i for i, servidor in enumerate(self.__servidores) if servidor.nome == servidor_a_ser_checado.nome), None)
        print(f'CHECANDO O {self._SanidadeCheck__servidores[indice_servidor]}')


    def add_servidor(self, servidor:Servidor):
        self.__servidores.append(servidor)


    def trocar_servidor(self, servidor_a_ser_trocado: Servidor, novo_servidor:Servidor):
        indice_servidor_a_ser_trocado = next((i for i, servidor in enumerate(self.__servidores) if servidor.nome == servidor_a_ser_trocado.nome), None)
        self.__servidores[indice_servidor_a_ser_trocado] = novo_servidor 


    def retorna_lista_de_servidores(self):
        for servidor in self.__servidores:
            print(servidor)


sanidade_1 = SanidadeCheck()
sanidade_2 = SanidadeCheck()

servidor_1 = Servidor(nome='Servidor 1')
servidor_2 = Servidor(nome='Servidor 2')

sanidade_1.add_servidor(servidor=servidor_1)
sanidade_1.add_servidor(servidor=servidor_2)

sanidade_1.retorna_lista_de_servidores()

servidor_3 = Servidor(nome='Servidor 3')

sanidade_2.trocar_servidor(servidor_a_ser_trocado=servidor_1, novo_servidor=servidor_3)

sanidade_1.retorna_lista_de_servidores()

sanidade_1.checar_servidor(servidor_a_ser_checado = servidor_3)

sanidade_2.retorna_lista_de_servidores()

