import pyglet
from math import sqrt
from classes.sorts import Sort_zone_cercle


class Champdebataille(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 800, "Combat")
        self.combattants = []
        self.select = None
        self.zones = []
        # c'est quoi cet attribut status ? Ici c'est un string, mais d'autres bouts de code le considèrent comme ayant 
        # des attributs pas de String...
        self.status = "perso"
        self.tour = 0

    def on_draw(self):
        self.clear()
        for creature in self.combattants:
            creature.draw()
        for zone in self.zones:
            zone.draw()
        if self.select is not None:
            self.select.draw_selected()

    def add_combattant(self, perso):
        self.combattants.append(perso)

    def add_zone(self, zone):
        self.zones.append(zone)

    def on_mouse_press(self, x, y, button, modifiers): # permet de supprimer les persos/sorts en cliquant dessus, le changement de status se fait avec SUPPR
        if self.status == 'remove':
            for i in self.combattants:
                if (x - i.position[0])**2 + (y - i.position[1])**2 <= i.taille**2:
                    if self.select == i and self.combattants.index(self.select) != len(self.combattants) - 1:
                        self.select = self.combattants[self.combattants.index(i) + 1]
                        self.status = 'perso'
                    elif self.select == i:
                        self.select = self.combattants[0]
                        self.status = 'perso'
                    self.combattants.remove(i)
            for i in self.zones:
                if (x - i.position[0])**2 + (y - i.position[1])**2 <= 15**2:
                    self.zones.remove(i)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.status == 'perso' and self.select is not None:
            if (x-self.select.position_save[0])**2 + (y-self.select.position_save[1])**2 <= self.select.speed**2:
                self.select.move((x, y))
        if self.status == 'sort':  # Pour bouger les sorts
            if (x-self.select.position_save[0])**2 + (y-self.select.position_save[1])**2 <= self.select.portée**2:
                self.zones[-1].move((x, y))

    def tour_order(self):
        self.combattants = sorted(self.combattants, key=lambda perso: perso.initiative)[
            ::-1
        ]

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            if self.select is None:
                self.tour_order()
                self.select = self.combattants[0]
            elif self.status == 'perso':
                i = self.combattants.index(self.select)
                self.select.position_tour = self.select.position
                self.select.position_save = self.select.position
                self.select.portée = self.select.portée_base
                self.select.speed = self.select.basespeed
                if i == len(self.combattants) - 1:
                    self.select = self.combattants[0]
                    self.tour += 1
                else:
                    self.select = self.combattants[i + 1]
            elif self.status == 'sort' or self.status == 'remove':
                self.status = 'perso'
        if symbol == pyglet.window.key.BACKSPACE:
            self.select.position = self.select.position_tour
            self.select.position_save = self.select.position_tour
            self.select.speed = self.select.basespeed
        if symbol == pyglet.window.key.SPACE:
            self.select.speed = self.select.speed - sqrt(
                (self.select.position[0] - self.select.position_save[0]) ** 2
                + (self.select.position[1] - self.select.position_save[1]) ** 2
            )
            self.select.position_save = self.select.position
        if symbol == pyglet.window.key.UP:
            self.select.portée += 1.5 * 10
        if symbol == pyglet.window.key.DOWN and self.select.portée >= 1.5 * 10:
            self.select.portée -= 1.5 * 10
        if symbol == pyglet.window.key.S:  # Pour passer en mode sort, le sort par defaut est un cercle pour le moment on peut pas le changer
            self.status = 'sort'
            new_sort = Sort_zone_cercle(15, self.select.position)
            self.zones.append(new_sort)
        if symbol == pyglet.window.key.DELETE:  # Pour passer en mode suppression
            self.status = 'remove'
