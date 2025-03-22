from abc import ABCMeta, abstractmethod

#AbstractFactory
class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def criar_pizza_nao_vegana(self):
        pass

    @abstractmethod
    def criar_pizza_vegana(self):
        pass


#ConcreteFactory
class PizzaBrasileira(PizzaFactory):
    def criar_pizza_nao_vegana(self):
        return PizzaCamarao()
    
    def criar_pizza_vegana(self):
        return PizzaMandioca()


#ConcreteFactory
class PizzaItaliana(PizzaFactory):
    def criar_pizza_nao_vegana(self):
        return PizzaCalabresa()
    
    def criar_pizza_vegana(self):
        return PizzaTomate()
    

#AbstractProduct
class PizzaVegana(metaclass=ABCMeta):
    @abstractmethod
    def preparar(self, PizzaVegana):
        pass


#AbstractProduct
class PizzaNaoVegana(metaclass=ABCMeta):
    @abstractmethod
    def servir(self, PizzaVegana):
        pass


#ConcreteProduct
class PizzaMandioca(PizzaVegana):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')


#ConcreteProduct
class PizzaCamarao(PizzaNaoVegana):
    def servir(self, PizzaVegana):
        print(f'{type(self).__name__} é servida com camarão na {type(PizzaVegana).__name__}')


#ConcreteProduct
class PizzaTomate(PizzaVegana):
    def preparar(self):
        print(f'Preparando {type(self).__name__}')


#ConcreteProduct
class PizzaCalabresa(PizzaNaoVegana):
    def servir(self, PizzaVegana):
        print(f'{type(self).__name__} é servida com calabresa na {type(PizzaVegana).__name__}')


#Client
class Pizzaria:
    def fazer_pizzas(self):
        for factory in [PizzaBrasileira, PizzaItaliana]:
            self.factory = factory()
            self.pizza_nao_vegana = self.factory.criar_pizza_nao_vegana()
            self.pizza_vegana = self.factory.criar_pizza_vegana()
            self.pizza_vegana.preparar()
            self.pizza_nao_vegana.servir(self.pizza_vegana)


pizzaria = Pizzaria()
pizzaria.fazer_pizzas()