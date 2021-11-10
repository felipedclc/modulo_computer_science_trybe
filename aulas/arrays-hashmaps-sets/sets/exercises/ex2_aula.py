# saber quantos pacotes de doces distribuir no dia de Cosme e Damião
def contar_criancas(amigos):
    conjunto_crianças = set()
    for pos_1, pos_2 in amigos:
        conjunto_crianças.add(pos_1)
        conjunto_crianças.add(pos_2)

    conjunto_crianças.discard("a")  # discarta o elemento "a"
    return len(conjunto_crianças)


if __name__ == "__main__":
    amigos = [("d", "a"), ("f", "z"), ("g", "i"), ("a", "e"), ("d", "u")]
    print(contar_criancas(amigos))
