# Separar palavras de acordo com a sua letra inicial

text = [
    "ana",
    "ama",
    "joao",
    "que",
    "ama",
    "jose",
    "mas",
    "jose",
    "nao",
    "ama",
    "ana",
]


def screening(names):
    new_hash = {}
    for name in names:
        first_char = name[0]
        if first_char not in new_hash:
            new_hash[first_char] = [name]
        else:
            new_hash[first_char] += [name]
    return new_hash


print(screening(text))
