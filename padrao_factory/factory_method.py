from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):
    @abstractmethod
    def __repr__(self):
        pass


class SecaoPessoal(Secao):
    def __repr__(self):
        return 'Seção Pessoal'
    

class SecaoAlbum(Secao):
    def __repr__(self):
        return 'Seção Álbum'
    

class SecaoProjeto(Secao):
    def __repr__(self):
        return 'Seção Projeto'
    

class SecaoPublicacao(Secao):
    def __repr__(self):
        return 'Seção Publicação'
    

class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass
    
    def get_secoes(self):
        return self.secoes
    
    def add_secao(self, secao):
        self.secoes.append(secao)


class LinkedIn(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjeto())
        self.add_secao(SecaoPublicacao())


class Facebook(Perfil):
    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoPublicacao())
        self.add_secao(SecaoAlbum())


def executar_criar_perfil():
    rede_social = input('Em qual rede social deseja criar o perfil? [1-Linkedin, 2-Facebook]: ')
    match rede_social:
        case '1':
            perfil = LinkedIn()
        case '2':
            perfil = Facebook()
        case _:
            print('Opção inválida')
            return
    print(f'Criando o perfil no {type(perfil).__name__}')
    print(f'O perfil tem as seções: {perfil.get_secoes()}')


executar_criar_perfil()
