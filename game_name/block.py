from .globals import *

from rogue.colors import *
from .entity import *


class Stone(Block):
    def __init__(self, x=0, y=0, bg=BACKGROUND, health=1):
        super().__init__(x, y, '%', 'Stone', GREY, bg)