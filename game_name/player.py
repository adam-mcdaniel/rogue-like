from rogue.colors import *
from .entity import *


class Player(Body):
    def __init__(self, x, y):
        super().__init__(x, y, '@', BRIGHT_WHITE, BACKGROUND, Archer, Xnuli)

    def update(self, screen, key):
        if key == 'w':
            self.move(0, -1)
        elif key == 'a':
            self.move(-1, 0)
        elif key == 's':
            self.move(0, 1)
        elif key == 'd':
            self.move(1, 0)
        elif key == ' ':
            pass
        elif key == '\n':
            inventory.getSelected().consume(self)

