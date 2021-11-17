""" Em jogos de tabuleiro que precisam de 2 dados de 6 lados, é
muito comum que quando a soma dos números da 7 algo especial aconteça.
Isso porque 7 é a soma mais provável

Receba uma lista de números que representam várias jogadas de um dado
de 6 lados. Sua missão é combinar as jogadas que somam 7. Ou seja, descubra
todas as duplas que é possível formar que somam 7.

Cada jogada só poderá ser combinada uma única vez com outra dupla
 """


def get_sevens(rolls):
    doubles = []
    num_doubles = 1
    for num_loop1 in rolls:
        for num_loop2 in rolls:
            if (num_loop1 + num_loop2) == 7:
                doubles.append((num_loop1, num_loop2))
                num_doubles += 1
    return set(doubles)


def get_sevens_prof(rolls):
    seen_before = set()
    answ = []

    for roll in rolls:
        if 7-roll in seen_before:
            answ.append((7-roll, roll))
            seen_before.discard(7-roll)
        else:
            seen_before.add(roll)

    return answ


if __name__ == "__main__":
    rolls = [1, 5, 3, 2, 6, 1, 4, 2, 6, 3, 1, 1]
    print(get_sevens(rolls))
    print(get_sevens_prof(rolls))
