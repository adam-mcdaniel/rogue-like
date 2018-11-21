import sys
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

curses.start_color()
curses.use_default_colors()

curses.curs_set(0)
curses.mousemask(1)

# curses.COLOR_BLACK = -1
bg = -1

class Screen():
    def __init__(self):
        self.blocking = False
        self.setBlocking(True)
        self.sprites = []
        self.bg = -1
        self.n = -1

    def __len__(self):
        return self.sprites.__len__()

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        try:
            self.n += 1
            return self.sprites[self.n]
        except:
            raise StopIteration

    def __getitem__(self, i):
        return self.sprites[i]

    def getMouse(self):
        pos = curses.getmouse()
        x, y = pos[1], pos[2]
        return x, y
        
    def append(self, sprite):
        self.sprites.append(sprite)

    def remove(self, sprite):
        self.sprites.remove(sprite)

    def clear(self):
        del self.sprites[:]

    def render(self):
        stdscr.clear()
        for sprite in self.sprites:
            if not sprite.hiding:
                sprite.render()
        stdscr.refresh()

    def setBG(*args):
        global bg

        if len(args) > 1:
            bg = args[-1]
        else:
            bg = args[0]

        curses.init_pair(abs(hash(bg)*31)+10, -1, bg)
        stdscr.bkgd(' ', curses.color_pair(abs(hash(bg)*31)+10))

    def getBG(*args):
        return bg

    def update(self):
        stdscr.clear()
        for sprite in self.sprites:
            if not sprite.hiding:
                sprite.render()
        stdscr.refresh()

    def setBlocking(self, blocking):
        self.blocking = blocking
        try:
            # curses.timeout(10)
            curses.halfdelay(not blocking)
            # stdscr.nodelay(int(not blocking))
        except:
            pass

    def getKey(*args):
        try:
            return stdscr.getkey()
        except:
            return None
            

    def getSize(*args):
        stdscr.refresh()
        width = curses.COLS - 1
        height = curses.LINES - 1
        return width, height
        
    def exit(self):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit(0)