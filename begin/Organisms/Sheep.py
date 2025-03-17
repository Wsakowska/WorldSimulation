from .Animal import Animal

class Sheep(Animal):
    def __init__(self, position=None, world=None):
        super(Sheep, self).__init__(None, position, world)
        self.initParams()

    def initParams(self):
        self.power = 3
        self.initiative = 4
        self.liveLength = 10
        self.powerToReproduce = 6
        self.sign = 'S'

    def clone(self):
        return Sheep()
