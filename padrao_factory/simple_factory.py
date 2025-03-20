from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass 


class Cachorro(Animal):
    def falar(self):
        print('Au')


class Gato(Animal):
    def falar(self):
        print('Miau')


class Ovelha(Animal):
    def falar(self):
        print('Bé')


#Factory (Fabrica)
class Fabrica:
    _animais = {
        'Cachorro': Cachorro,
        'Gato': Gato,
        'Ovelha': Ovelha
    }
    def criar_animal_falante(self, animal:str):
        return self._animais[animal]().falar()
    

#Cliente
if __name__ == '__main__':
    fabrica = Fabrica()
    resposta_pergunta_animal_que_sera_criado = (
        input('Qual animal deseja criar? Digite 1 para Cachorro, 2 para Gato e 3 para Ovelha:')
    )
    match resposta_pergunta_animal_que_sera_criado:
        case '1': 
            animal = fabrica.criar_animal_falante('Cachorro')
        case '2': 
            animal = fabrica.criar_animal_falante('Gato')
        case '3': 
            animal = fabrica.criar_animal_falante('Ovelha')
        case _:
            print('Opção inválida')

#Nesse padrao as classes ficam somente dentro de factory(fabrica), o cliente nao instancia elas, ele so tem acesso a factory




