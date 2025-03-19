class MetaclasseSingleton(type):
    __instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super(MetaclasseSingleton, self).__call__(*args, **kwargs)
        return self.__instances[self]
    

class Logger(metaclass=MetaclasseSingleton):
    pass


logger_1 = Logger()
print(f'Logger 1: {id(logger_1)}')

logger_2 = Logger()
print(f'Logger 2: {id(logger_2)}')