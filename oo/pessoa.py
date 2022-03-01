class Pessoa:

    def __init__(self, *filhos, nome: str, idade=35, peso=35):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.filhos = list(filhos)

    def cumprimentar(self):

        return f'Olá {id(self)}'


if __name__ == '__main__':

    print(Pessoa.cumprimentar(usuario))
    print(id(usuario))
    print(usuario.cumprimentar())

    usuario= Pessoa(nome='Bam')
    #usuario.nome = 'Liane'
    print(f'Nome: {usuario.nome} - Idade: {usuario.idade} - Peso: {usuario.peso}')

    amanda = Pessoa(nome='Amanda', idade=32, peso=67.52)
    luciano = Pessoa(amanda, nome='Luciano')

    for filho in luciano.filhos:
        print(filho.nome)



