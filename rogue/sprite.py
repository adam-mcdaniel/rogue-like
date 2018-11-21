import curses
from .colors import *
from .modes import *
from .screen import stdscr
from .screen import Screen

class Sprite():
    def __init__(self, x, y, text=' ', fg=WHITE, bg=Screen.getBG(), mode=NORMAL):
        self.x = x
        self.y = y
        self.text = text
        self.fg = fg
        self.bg = bg
        self.hiding = False
        self.setFG(fg)
        self.setBG(bg)
        self.mode = mode

    def update(self, *args):
        pass

    def pos(self):
        return self.x, self.y

    def setText(self, text):
        self.text = text

    def setMode(self, mode):
        self.mode = mode

    def setFG(self, color):
        curses.init_pair(abs(hash(self.fg+2) * hash(self.bg+2)), self.fg, self.bg);
        self.fg = color

    def setBG(self, color):
        curses.init_pair(abs(hash(self.fg+2) * hash(self.bg+2)), self.fg, self.bg);
        self.bg = color

    def move(self, x, y):
        self.x += x
        self.y += y

    def goto(self, x, y):
        self.x = x
        self.y = y

    def hide(self):
        self.hiding = True

    def show(self):
        self.hiding = False

    def render(self):
        w = curses.COLS - 1
        h = curses.LINES - 1

        if self.hiding or self.x < 0 or self.x > w or self.y < 0 or self.y > h:
            pass
        else:
            try:
                if self.mode:
                    stdscr.addstr(self.y, self.x, self.text, curses.color_pair(abs(hash(self.fg+2) * hash(self.bg+2))) | self.mode)
                else:
                    stdscr.addstr(self.y, self.x, self.text, curses.color_pair(abs(hash(self.fg+2) * hash(self.bg+2))))
            except:
                pass