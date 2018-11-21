from .entity import *


class Body(Entity):
    def __init__(self, x, y, text, fg, bg, archetype, race):
        super().__init__(x, y, text, fg, bg, archetype, race)
        # self.show()

    def move(self, x, y):
        save_x, save_y = self.pos()
        self.x += x
        self.y += y
        for sprite in screen:
            if isinstance(sprite, Block):
                if sprite.pos() == self.pos():
                    self.goto(save_x, save_y)
                    break