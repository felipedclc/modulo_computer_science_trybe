from collections.abc import Iterable, Iterator


class Estudante:
    def __init__(self, nome, estado):
        self.nome = nome
        self.estado = estado

    def __repr__(self):  # funciona como o toString(Java)
        return f"Estudante {self.nome} que mora em {self.estado}"


class ListaEstudantes(Iterable):
    def __init__(self, turma=None):
        self.turma = turma
        self.__lista_estudantes = []

    def insere_estudante(self, estudante):
        self.__lista_estudantes.append(estudante)

    def __str__(self):
        return str(self.__lista_estudantes)

    def __iter__(self):
        return IteratorEstudantes(self.__lista_estudantes)

    def escolhe_dupla(self, estrategia=None):
        if not estrategia:
            estrategia = GeraDuplas
        return estrategia.gera_uma_dupla(self.__lista_estudantes)


class GeraDuplas:
    # staticmethod: usado para funções internas da classe
    # pois não precisa de instância(init, self)
    @staticmethod
    def gera_uma_dupla(lista_estudantes):
        return tuple(lista_estudantes[:2])


class GeraDuplasEstados:
    @staticmethod
    def gera_uma_dupla(lista_estudantes):
        for indice, estudante1 in enumerate(lista_estudantes):
            for estudante2 in lista_estudantes[indice + 1]:
                if estudante1.estado == estudante2.estado:
                    return (estudante1, estudante2)


class IteratorEstudantes(Iterator):
    def __init__(self, lista_estudantes):
        self.lista_estudantes = lista_estudantes
        self.contador = -1

    def __next__(self):
        """Retorna um estudante de cada vez"""
        self.contador += 1
        try:
            return self.lista_estudantes[self.contador]
        except IndexError:
            raise StopIteration  # encerra a iteração
