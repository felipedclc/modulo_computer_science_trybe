class Tv:
    def __init__(self, tamanho):
        self.__volume = 50  # __protected
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        volume_max = 99
        print(f"volume: {self.__volume}")
        self.__volume += 1 if self.__volume <= volume_max else print("MAX")

    def diminuir_volume(self):
        volume_min = 0
        print(f"volume: {self.__volume}")
        self.__volume -= 1 if self.__volume >= volume_min else print("MIN")

    def muda_canal(self, canal):
        if 1 <= self.__canal <= 99:
            self.__canal = canal
        else:
            raise ValueError("Selecione canais entre 1 e 99")

    def ligar_desligar(self):
        self.__ligada = not self.__ligada
        """ if self.__ligada is True:
            self.__ligada = False
        else:
            self.__ligada is True """


# instanciando Tv:
tv1 = Tv(100)
tv1.aumentar_volume()
print(vars(tv1))
