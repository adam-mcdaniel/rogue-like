from .globals import *

from rogue.colors import *
from .entity import *

from .land import *
from .entity import *
from .bunny import Bunny
from .player import Player

class Crosshair(Entity):
    def __init__(self):
        super().__init__(0, 0, 'X', BRIGHT_RED, BACKGROUND, Archetype, Race)
        self.hide()

    def update(self, key):
        if key == 'i':
            self.show()
            screen.setBlocking(False)
            while True:
                key = screen.getKey()
                if key in ['i', 'q']:
                    break

                elif key == '\n':
                    for sprite in screen:
                        if sprite.pos() == self.pos():
                            if isinstance(sprite, Grass):
                                info.addSentence('This is grass.')
                            elif isinstance(sprite, Flower):
                                info.addSentence('This is a flower.')
                            elif isinstance(sprite, Player):
                                info.addSentence('This is you.')
                            elif isinstance(sprite, Bunny):
                                info.addSentence('This is a bunny.')
                
                self.goto(*screen.getMouse())
                screen.update()

            screen.setBlocking(True)
            self.hide()

