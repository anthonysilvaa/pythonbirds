class Pessoa:

    def cumprimentar(self):

        return f'Olá {id(self)}'


if __name__ == '__main__':

    usuario = Pessoa()
    print(Pessoa.cumprimentar(usuario))
    print(id(usuario))
    print(usuario.cumprimentar())