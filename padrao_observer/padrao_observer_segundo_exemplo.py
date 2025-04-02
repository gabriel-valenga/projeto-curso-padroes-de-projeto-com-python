from abc import ABCMeta, abstractmethod

#Assunto/topico
class AgenciaNoticias:
    def __init__(self):
        self.__inscritos = []
        self.__ultima_noticia = None 


    def inscrever(self, inscrito):
        self.__inscritos.append(inscrito)


    def desinscrever(self, inscrito):
        self.__inscritos.remove(inscrito)


    def notificar_todos(self):
        for inscrito in self.__inscritos:
            inscrito.notificar()


    def adicionar_noticia(self, noticia):
        self.__ultima_noticia = noticia


    def mostrar_noticia(self):
        return f'Urgente: {self.__ultima_noticia}'
    

    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]
    

#Interface Observer
class TipoInscricao(metaclass=ABCMeta):
    @abstractmethod
    def notificar(self):
        pass


#Observador A
class InscritosSms(TipoInscricao):
    def __init__(self, agencia_noticias):
        self.agencia_noticias = agencia_noticias
        self.agencia_noticias.inscrever(self)


    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticias.mostrar_noticia()}')


#Observador B
class InscritosEmail(TipoInscricao):
    def __init__(self, agencia_noticias):
        self.agencia_noticias = agencia_noticias
        self.agencia_noticias.inscrever(self)


    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticias.mostrar_noticia()}')


#Observador N
class InscritosOutroMeio(TipoInscricao):
    def __init__(self, agencia_noticias):
        self.agencia_noticias = agencia_noticias
        self.agencia_noticias.inscrever(self)


    def notificar(self):
        print(f'{type(self).__name__} {self.agencia_noticias.mostrar_noticia()}')
    

#Cliente
if __name__ == '__main__':
    agencia_noticias = AgenciaNoticias()
    inscritos_sms = InscritosSms(agencia_noticias)
    inscritos_email = InscritosEmail(agencia_noticias)
    inscritos_outro_meio = InscritosOutroMeio(agencia_noticias)
    print(f'Inscritos: {agencia_noticias.inscritos()}')
    agencia_noticias.adicionar_noticia('Novo curso na Geek University.')
    agencia_noticias.notificar_todos()
    agencia_noticias.desinscrever(inscrito=inscritos_sms)
    print(f'Desinscrito: {type(inscritos_sms).__name__}')
    print(f'Inscritos: {agencia_noticias.inscritos()}')