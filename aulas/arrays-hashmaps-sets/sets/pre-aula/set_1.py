A = {"xablau": 1, "a": 2, "b": 3}
print("xablau" not in A)  # verifica se a chave xablau existe no arr


# Criando a classe Conjunto
class Conjunto:
    def __init__(self):
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, value):
        if not self.set[value]:
            self.set[value] = True
        if value > self.last_element:
            self.last_element = value

    def __str__(self):
        string = "{"

        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string


if __name__ == "__main__":
    conjunto_1 = Conjunto()
    for el in [0, 10, 100, 1000]:
        conjunto_1.add(el)

    print(conjunto_1)
