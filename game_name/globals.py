from rogue.colors import *
from rogue.screen import Screen

Screen.setBG(BACKGROUND)

from .menu import *

w, h = Screen.getSize()
screen = Screen()

WIN_WIDTH = w - int(w/3)
WIN_HEIGHT = 24


inventory = Menu(screen, 0, 0, int(w/6), h, fg=GREY, bg=BLACK)
info = DialogBox(screen, int(w - int(w/6))+1, 0, int(w/6), h, fg=BRIGHT_WHITE, bg=BLACK)