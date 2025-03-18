class Singleton:
    __instance = None


    def __init__(self):
        if not Singleton.__instance:
            print(f'O método __init__ foi chamado... id: {id(self)}')
        else:
            print(f'A instância já foi criada: {self.get_instance()} | id: {id(self)}')


    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        print(f'id: {id(cls)}')
        return cls.__instance
    

s1 = Singleton() # a classe é inicializada, mas o objeto não é criado.

print(f'Objeto criado agora: {Singleton.get_instance()}')

s2 = Singleton() # instância já criada