class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def cumprimentar(self):

        return f'Olá {id(self)}'


if __name__ == '__main__':

    usuario = Pessoa('Amanda', 32, 67.52)

    usuario.nome = 'Liane'

    print(f'Nome: {usuario.nome} - Idade: {usuario.idade} - Peso: {usuario.peso}')

    print(Pessoa.cumprimentar(usuario))
    print(id(usuario))
    print(usuario.cumprimentar())