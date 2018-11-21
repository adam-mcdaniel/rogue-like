from game_name.globals import *

from random import randint

from rogue.colors import *
from rogue.sprite import Sprite

from game_name.block import *
from game_name.tools import *

from game_name.menu import Menu, DialogBox
from game_name.land import *
from game_name.bunny import Bunny
from game_name.player import Player
from game_name.entity import *
from game_name.crosshair import Crosshair


for x in range(-250, 250):
    for y in range(-250, 250):
        if not randint(0, 45):
            if not randint(0, 10):
                if not randint(0, 1):
                    screen.append(Bunny(x+randint(-5, 5), y+randint(-5, 5)))
                screen.append(Flower(x, y))
            else:
                screen.append(Grass(x, y))

        if not randint(0, 10000):
            if not randint(0, 3):
                screen.append(Pickaxe(x+5, y+5))
            
            for x_ in range(0, 10):
                screen.append(Stone(x+x_, y))
                
            for y_ in range(0, 10):
                screen.append(Stone(x, y+y_))
                screen.append(Stone(x+9, y+y_))


player = Player(0, 0)
screen.append(player)

crosshair = Crosshair()
screen.append(crosshair)

info.start()
info.addText('You awake')
info.addText('in a field')

inventory.start()
h_ = Hand()
h_.hide()
inventory.addOption(h_.name, h_)

def main():
    n = 0
    focus(screen, player)
    while True:
        

        screen.update()
        
        key = screen.getKey()

        crosshair.update(key)
        if key in ['w', 'a', 's', 'd', ' ', '\n']:
            player.update(screen, key)

            for sprite in screen:
                if isinstance(sprite, Bunny):
                    sprite.update(screen)

        if key == u"\u0008":
            screen.exit()
        
        if key in ['[', ']']:
            inventory.update(key)
            info.addSentence('You equip '+inventory.getSelected().name)

        focus(screen, player)


if __name__ == "__main__":
    main()
