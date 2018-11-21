from rogue.colors import *
from .entity import *

from random import randint

class Flower(Entity):
    def __init__(self, x, y):
        if not randint(0, 1):
            super().__init__(x, y, '*', fg=BRIGHT_YELLOW)
        else:
            super().__init__(x, y, '*', fg=YELLOW)

class Grass(Entity):
    def __init__(self, x, y):
        if not randint(-1, 1):
            if not randint(0, 1):
                super().__init__(x, y, '^', fg=GREEN)
            else:
                super().__init__(x, y, '#', fg=GREEN)
        else:
            if not randint(0, 1):
                super().__init__(x, y, '^', fg=BRIGHT_GREEN)
            else:
                super().__init__(x, y, '#', fg=BRIGHT_GREEN)