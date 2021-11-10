from lista_estudantes import Estudante, ListaEstudantes

if __name__ == "__main__":
    tio_lipe = Estudante("Felipe", "MG")
    print(tio_lipe)

    turma_9 = ListaEstudantes(turma=9)
    turma_9.insere_estudante(tio_lipe)
    turma_9.insere_estudante(Estudante("José", "RJ"))
    turma_9.insere_estudante(Estudante("Ana", "SP"))
    turma_9.insere_estudante(Estudante("Fran", "MG"))
    print(turma_9)

    # iterando uma classe após usar Iterable e Iterator
    estados_unicos = {estudante.estado for estudante in turma_9}
    print(f"{estados_unicos=} ")
