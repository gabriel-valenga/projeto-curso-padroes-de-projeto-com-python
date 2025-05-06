from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):

    @abstractmethod
    def manipular(self):
        pass 


class StateConcretoA(State):

    def manipular(self):
        print('StateConcretoA')


class StateConcretoB(State):

    def manipular(self):
        print('StateConcretoB')


class Context():
    
    def __init__(self):
        self.state = None 


    def get_state(self):
        return self.state
    

    def set_state(self, state):
        self.state = state


    def manipular(self):
        self.state.manipular()


contexto = Context()
state_a = StateConcretoA()
state_b = StateConcretoB()
contexto.set_state(state_a)
contexto.manipular()
contexto.set_state(state_b)
contexto.manipular()
