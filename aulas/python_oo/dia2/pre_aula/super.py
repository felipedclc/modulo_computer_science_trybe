class Pai(object):
    def __init__(self):
        print("Construindo a classe Pai")


class Filha(Pai):
    def __init__(self):
        super(Filha, self).__init__()
