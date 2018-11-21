from .globals import *
from rogue.screen import Screen
from rogue.sprite import Sprite

from .classes import *


class Entity(Sprite):
    def __init__(self, x, y, text, fg=-1, bg=Screen.getBG(), archetype=Archetype, race=Race):
        super().__init__(x, y, text, fg, bg)
        self.health = 10
        self.health_capacity = 10

        self.inventory = []

        self.archetype = archetype(self)
        self.race = race(self)

        self.level = 0
        self.xp = 0
        
        self.current_tool = None
        
        self.attractiveness = 0
        self.luck = 0
        self.armor = 0
        self.mana = 0
        self.ego = 0
        self.user_hidden = False

    def hide(self):
        super().hide()
        self.user_hidden = True

    def show(self):
        super().show()
        self.user_hidden = False

    def hide_(self):
        super().hide()

    def setTool(self, tool):
        self.current_tool = tool

    def getTool(self):
        return self.current_tool

    def dealDamage(self, damage):
        self.health -= (damage - self.armor)
        self.armor -= 1

    def heal(self, health):
        self.health += health
        self.health = min(self.health_capacity, self.health)

    def addHealth(self, n):
        self.health_capacity += n

    def addArmor(self, n):
        self.armor += n

    def addEgo(self, n):
        self.ego += n

    def addLuck(self, n):
        self.luck += n

    def addMana(self, n):
        self.mana += n

    def addXP(self, xp):
        self.xp += xp
        if self.xp > self.level * 1000:
            self.addLevel()

    def addLevel(self):
        self.level += 1

    def get(self, parent):
        parent.inventory.append(self)

    def consume(self, parent):
        return True


class Block(Entity):
    def __init__(self, x, y, text='#', name='block', fg=WHITE, bg=BACKGROUND, health=1):
        super().__init__(x, y, text, fg, bg, Archetype, Race)
        self.health_cap = health
        self.health = health
        self.name = name
    
    def consume(self, parent):
        inventory.removeOption(self.name)
        self.goto(*parent.pos())
        self.show()
        screen.append(self)
        return True

    def get(self, parent):
        if parent.getTool():
            self.dealDamage(parent.getTool().damage)
            if self.health <= 0:
                super().get(parent)
                self.health = self.health_cap
                self.hide()
                screen.remove(self)
                inventory.addOption(self.name, self)
            else:
                pass


class Tool(Entity):
    def __init__(self, x=0, y=0, text='#', name='tool', fg=WHITE, bg=BACKGROUND, health=1, damage=1):
        super().__init__(x, y, text, fg, bg, Archetype, Race)
        self.health = health
        self.damage = damage
        self.name = name
    
    def consume(self, parent):
        parent.setTool(self)
        if self.health >= 0:
            for sprite in screen:
                if isinstance(sprite, Block):
                    if abs(sprite.x - parent.x) < 1 and abs(sprite.y - parent.y) <= 1:
                        self.dealDamage(1)
                        sprite.get(parent)
                        break
                    if abs(sprite.x - parent.x) <= 1 and abs(sprite.y - parent.y) < 1:
                        self.dealDamage(1)
                        sprite.get(parent)
                        break
        else:            
            inventory.removeOption(self.name)
    

    def get(self, parent):
        super().get(parent)
        self.hide()
        screen.remove(self)
        inventory.addOption(self.name, self)


class Body(Entity):
    def __init__(self, x, y, text, fg, bg, archetype, race):
        super().__init__(x, y, text, fg, bg, archetype, race)

    def move(self, x, y):
        save_x, save_y = self.pos()
        super().move(x, y)
        for sprite in screen:
            if isinstance(sprite, Block):
                if sprite.pos() == self.pos():
                    self.goto(save_x, save_y)
                    break


def focus(scrn, focused_sprite, w=0, h=0):
    global WIN_WIDTH, WIN_HEIGHT
    if not w:
        w, _ = scrn.getSize()
    if not h:
        _, h = scrn.getSize()

    WIN_WIDTH = min(w, WIN_WIDTH)
    WIN_HEIGHT = min(h, WIN_HEIGHT)


    x_distance, y_distance = int(w/2) - focused_sprite.x, int(h/2) - focused_sprite.y
    if focused_sprite.x != int(w/2) or focused_sprite.y != int(h/2):
        for sprite in scrn:
            if isinstance(sprite, Entity):
                sprite.goto(sprite.x + x_distance,
                            sprite.y + y_distance)
                            
                if (sprite.x < w/2 - WIN_WIDTH/2) or (sprite.x > w/2 + WIN_WIDTH/2):
                    sprite.hide_()
                elif (sprite.y < h/2 - WIN_HEIGHT/2) or (sprite.y > h/2 + WIN_HEIGHT/2):
                    sprite.hide_()
                else:
                    if not sprite.user_hidden:
                        sprite.show()