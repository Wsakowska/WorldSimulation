import logging
from .Animal import Animal
from Position import Position
from Action import Action
from ActionEnum import ActionEnum

class Lynx(Animal):
    def __init__(self, position=None, world=None):
        super().__init__(None, position, world)
        self.initParams()

    def initParams(self):
        self.power = 6
        self.initiative = 5
        self.liveLength = 18
        self.initialLiveLength = 18 
        self.powerToReproduce = 14
        self.sign = 'R'

    def clone(self):
        return Lynx(position=self.position, world=self.world)
