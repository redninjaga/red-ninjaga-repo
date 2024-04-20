class Lol:
    def __init__(self, position):
        self.position = position

    def plus(self):
        print(self.position[0]+10, self.position[1]+10, self.position[2]+100)

kek = Lol((10,20,30))
kek.plus()
