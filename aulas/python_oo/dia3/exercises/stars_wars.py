class Soldier:
    def __init__(self, level):
        self.level = level

    def attack(self):
        return self.level * 1


class Jedi:
    def __init__(self, level):
        self.level = level

    def attackWithSaber(self):
        return self.level * 100


# pega o parámetro "jedi" e muda o attackWithSaber para attack
class JediAdapter:
    def __init__(self, jedi):
        self.jedi = jedi

    def attack(self):
        return self.jedi.attackWithSaber()


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(f"You caused {self.character.attack()} of damage in the enemy")


if __name__ == "__main__":
    StarWarsGame(Soldier(5)).fight_enemy()
    StarWarsGame(JediAdapter(Jedi(20))).fight_enemy()
