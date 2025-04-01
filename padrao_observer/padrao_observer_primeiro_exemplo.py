class Objeto:
    def __init__(self):
        self.__observadores = []


    def __repr__(self):
        return '::Objeto::'
    

    def registrar(self, observador):
        self.__observadores.append(observador)


    def notificar_alteracoes_aos_observadores(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)


class ObservadorA:
    def __init__(self, objeto):
        objeto.registrar(self)


    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {objeto}')


class ObservadorB:
    def __init__(self, objeto):
        objeto.registrar(self)


    def notificar(self, objeto, *args):
        print(f'O {type(self).__name__} recebeu uma {args[0]} de {objeto}')


objeto = Objeto()
observador_a = ObservadorA(objeto)
observador_b = ObservadorB(objeto)
objeto.notificar_alteracoes_aos_observadores('notificação')
