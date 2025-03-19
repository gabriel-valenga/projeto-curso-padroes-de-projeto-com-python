import sqlite3


class Singleton(type):
    __instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self.__instances:
            self.__instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self.__instances[self]
    

class Database(metaclass=Singleton):
    connection = None 

    def connect(self):
        if not self.connection:
            print('Não há conexão criada, conexão será criada agora.')
            self.connection = sqlite3.connect('db.geek')
            self.cursor = self.connection.cursor()
        return self.cursor
    

    def close(self):
        if self.connection:
            print('Conexão será fechada agora.')
            self.connection.close()
            self.connection = None 
            self.cursor = None


db1 = Database()
db1.connect()
db2 = Database()
db2.connect()
db2.close()
db3 = Database()
db3.connect()