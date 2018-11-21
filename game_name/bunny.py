from .globals import *

from rogue.colors import *
from .entity import *
from .block import *


from random import randint


class Bunny(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 'b', GREY, BACKGROUND, Archetype, Race)

    def update(self, *args):
        x = randint(-1, 1)
        y = randint(-1, 1)

        save_x, save_y = self.pos()
        self.move(x, y)

        # for sprite in screen:
        #     if isinstance(sprite, Block):
        #         if sprite.pos() == self.pos():
        #             self.goto(save_x, save_y)
        #             break
