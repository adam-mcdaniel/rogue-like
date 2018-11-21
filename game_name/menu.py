from rogue.screen import Screen
from rogue.sprite import Sprite
from rogue.colors import *
from rogue.modes import *

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


class Menu():
    def __init__(self, screen, x, y, w=Screen.getSize()[0], h=Screen.getSize()[1], fg=BRIGHT_RED, bg=BRIGHT_CYAN):
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.fg = fg
        self.bg = bg

        self.screen = screen
        self.selected = 0
        self.options = {}
        self.sprites = []

    def start(self):
        top_bottom_borders = "+" + "-"*max(0, self.w-2) + "+"
        middle = "|" + " "*max(0, self.w-2) + "|"
        self.screen.append(Sprite(self.x, self.y, top_bottom_borders, fg=BRIGHT_BLUE, bg=self.bg))
        for z in range(self.y+1, self.y+self.h):
            self.screen.append(Sprite(self.x, z, middle, fg=BRIGHT_BLUE, bg=self.bg))
        self.screen.append(Sprite(self.x, self.y+self.h, top_bottom_borders, fg=BRIGHT_BLUE, bg=self.bg))

    def update(self, key):
        if key == '[':
            self.selected = max(0, self.selected)
            self.selected = min(len(self.options)-1, self.selected)
            self.sprites[self.selected].setMode(NORMAL)
            self.selected -= 1
            self.selected = max(0, self.selected)
            self.selected = min(len(self.options)-1, self.selected)
            self.sprites[self.selected].setMode(HIGHLIGHT)
        if key == ']':
            self.selected = max(0, self.selected)
            self.selected = min(len(self.options)-1, self.selected)
            self.sprites[self.selected].setMode(NORMAL)
            self.selected += 1
            self.selected = max(0, self.selected)
            self.selected = min(len(self.options)-1, self.selected)
            self.sprites[self.selected].setMode(HIGHLIGHT)

    def addOption(self, option, value):
        while option in self.options:
            option += ' '

        value.name = option

        self.options[option] = value
            
        s = Sprite(self.x+1, min(self.y + len(self.sprites)+1, self.h - 1), option.split()[0], fg=self.fg, bg=self.bg)
        self.sprites.append(s)
        self.screen.append(s)

        self.sprites[min(self.selected, self.h - 2)].setMode(HIGHLIGHT)

    def removeOption(self, option):
        self.selected -= 1
        self.selected = max(0, self.selected)
        self.selected = min(len(self.options)-1, self.selected)
        index = list(self.options.keys()).index(option)
        self.options = removekey(self.options, option)
        self.screen.remove(self.sprites[index])
        del self.sprites[index]
        for sprite in self.sprites[index:]:
            sprite.move(0, -1)
        self.sprites[self.selected].setMode(HIGHLIGHT)

    def getSelected(self):
        return self.options[list(self.options.keys())[self.selected]]
        

class DialogBox():
    def __init__(self, screen, x, y, w=Screen.getSize()[0], h=Screen.getSize()[1], fg=BRIGHT_RED, bg=BRIGHT_CYAN):
        # for x in range(x, x+w):
        self.x = x
        self.y = y

        self.w = w
        self.h = h

        self.fg = fg
        self.bg = bg

        self.screen = screen
        self.sprites = []

    def start(self):
        top_bottom_borders = "+" + "-"*max(0, self.w-2) + "+"
        middle = "|" + " "*max(0, self.w-2) + "|"
        self.screen.append(Sprite(self.x, self.y, top_bottom_borders, fg=BRIGHT_BLUE, bg=self.bg))
        for z in range(self.y+1, self.y+self.h):
            self.screen.append(Sprite(self.x, z, middle, fg=BRIGHT_BLUE, bg=self.bg))
        self.screen.append(Sprite(self.x, self.y+self.h, top_bottom_borders, fg=BRIGHT_BLUE, bg=self.bg))

    def greyOut(self):
        for sprite in self.sprites:
            sprite.setFG(GREY)

    def addText(self, text):
        if len(self.sprites) > self.h-2:
            self.removeTop()
        s = Sprite(self.x+1, self.y + len(self.sprites)+1, text, fg=self.fg, bg=self.bg)
        self.sprites.append(s)
        self.screen.append(s)

    def removeTop(self):
        self.screen.remove(self.sprites[0])
        del self.sprites[0]
        for sprite in self.sprites:
            sprite.move(0, -1)

    def addSentence(self, text):
        self.greyOut()
        sentence = text.split()
        buf = ''
        while len(sentence) != 0:
            buf += sentence[0] + ' '
            del sentence[0]
            if len(buf) >= self.w - 4 or len(sentence) == 0:
                self.addText(buf)
                buf = ''

    def getLast(self):
        return self.sprites[-1].text