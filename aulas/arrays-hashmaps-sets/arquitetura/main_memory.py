class MainMemory:
    def __init__(self):
        self.clean()

    def load(self, value):
        self.loaded_memory.append(value)

    def get(self, index):
        if index > len(self.loaded_memory):
            return 0
        return self.loaded_memory[index]

    def clean(self):
        self.loaded_memory = []


memory = MainMemory()
memory.load([1, 2, 3, 4])
print(memory.get(4))
