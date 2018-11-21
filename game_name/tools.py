from .globals import *

from rogue.colors import *
from .entity import *
from .block import *


class Hand(Tool):
    def __init__(self, damage=1):
        super().__init__(text=' ', name='Hand', fg=YELLOW, bg=BACKGROUND)
        self.damage = damage
        self.health = 1000000000000000000000000000

    def consume(self, parent):
        super().consume(parent)
        self.health = 1000000000000000000000000000
        for sprite in screen:
            if isinstance(sprite, Tool):
                if sprite.pos() == parent.pos():
                    sprite.get(parent)
                    break


class Pickaxe(Tool):
    def __init__(self, x, y, damage=10):
        super().__init__(x=x, y=y, text='|', name='Pickaxe', fg=YELLOW, bg=BACKGROUND)
        self.damage = damage
        self.health = 100