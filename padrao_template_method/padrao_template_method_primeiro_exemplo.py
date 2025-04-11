from abc import ABCMeta, abstractmethod 


class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar_codigo_fonte(self):
        pass


    @abstractmethod
    def compilar_objeto(self):
        pass

    @abstractmethod
    def executar(self):
        pass     


    def compilar_e_executar(self): #template method
        self.coletar_codigo_fonte()
        self.compilar_objeto()
        self.executar()


class CompiladorIos(Compilador):

    def coletar_codigo_fonte(self):
        print('Coletando código fonte Swift...')


    def compilar_objeto(self):
        print('Compilando código Swift para bytecode LLVM...')


    def executar(self):
        print('Programa IOS executando no ambiente de execução...')   


class CompiladorAndroid(Compilador):

    def coletar_codigo_fonte(self):
        print('Coletando código fonte Kotlin...')


    def compilar_objeto(self):
        print('Compilando código Kotlin para bytecode JVM...')


    def executar(self):
        print('Programa Android executando no ambiente de execução...')   
        

ios = CompiladorIos()
ios.compilar_e_executar()
android = CompiladorAndroid()
android.compilar_e_executar()