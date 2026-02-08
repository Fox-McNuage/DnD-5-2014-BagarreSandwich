import pyglet
from math import sqrt


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

    def on_mouse_release(self, x, y, button, modifiers):
        if self.status != "perso":
            if self.status.terrain:
                self.add_zone(self.status)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print(self.select)
        if self.status == "perso" and self.select is not None:
            if (x - self.select.position_save[0]) ** 2 + (
                y - self.select.position_save[1]
            ) ** 2 <= self.select.speed**2:
                self.select.move((x, y))
        else:
            pass
            # c'est censé vouloir dire quoi ça même ?
            # self.status.position = (x, y) 

    def tour_order(self):
        self.combattants = sorted(self.combattants, key=lambda perso: perso.initiative)[
            ::-1
        ]

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ENTER:
            if self.select is None:
                self.tour_order()
                self.select = self.combattants[0]
            else:
                i = self.combattants.index(self.select)
                self.select.position_tour = self.select.position
                self.select.position_save = self.select.position
                self.select.portée = self.select.portée_base
                if i == len(self.combattants) - 1:
                    self.select = self.combattants[0]
                    self.tour += 1
                else:
                    self.select = self.combattants[i + 1]
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
