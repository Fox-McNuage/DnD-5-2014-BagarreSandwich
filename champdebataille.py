import pyglet
from math import sqrt


class Champdebataille(pyglet.window.Window):
    def __init__(self):
        super().__init__(800, 800, "Combat")
        self.combattants = []
        self.select = None
        self.zones = []
        self.status = 'perso'
        self.tour = 0

    def on_draw(self):
        self.clear()
        for i in self.combattants:
            i.draw()
        for i in self.zones:
            i.draw()
        if self.select != None:
            self.select.draw_selected()

    def add_combattant(self, perso):
        self.combattants.append(perso)

    def add_zone(self, zone):
        self.zones.append(zone)


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.status == 'perso':
            if (x-self.select.position_save[0])**2 + (y-self.select.position_save[1])**2 <= self.select.speed**2:
                self.select.move((x, y))
        if self.status == 'sort':
            if (x-self.select.position_save[0])**2 + (y-self.select.position_save[1])**2 <= self.select.portée**2:
                self.zones[-1].move((x, y))

    def on_mouse_press(self, x, y, button, modifiers):
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

    def tour_order(self):
        self.combattants = sorted(self.combattants, key=lambda perso: perso.initiative)[::-1]

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
            self.select.speed = self.select.speed - sqrt((self.select.position[0] - self.select.position_save[0])**2 + (self.select.position[1] - self.select.position_save[1])**2)
            self.select.position_save = self.select.position
        if symbol == pyglet.window.key.UP:
            self.select.portée += 1.5*10
        if symbol == pyglet.window.key.DOWN and self.select.portée >= 1.5*10:
            self.select.portée -= 1.5*10
        if symbol == pyglet.window.key.S:
            self.status = 'sort'
            new_sort = Sort_zone_cercle(15, self.select.position)
            self.zones.append(new_sort)
        if symbol == pyglet.window.key.DELETE:
            self.status = 'remove'


class Personnage:
    def __init__(self, nom="", couleur=(0, 102, 204, 255), taille=1.5, allonge=1.5, basespeed=9, position=(0, 0), portée=0, initiative=5):
        self.couleur = couleur
        self.taille = taille*10
        self.nom = nom
        self.allonge = allonge*10
        self.position = position
        self.position_save = position
        self.position_tour = position
        self.basespeed = basespeed*10
        self.speed = basespeed*10
        self.portée_base = portée*10
        self.portée = portée
        self.initiative = initiative

    def draw(self):
        pyglet.shapes.Circle(self.position[0], self.position[1], self.taille + self.allonge, color=(204, 0, 0, 150)).draw()
        pyglet.shapes.Circle(self.position[0], self.position[1], self.taille, color=self.couleur).draw()

    def draw_selected(self):
        pyglet.shapes.Arc(self.position_save[0], self.position_save[1], self.taille + self.speed, closed=True, color=(0, 204, 0, 150)).draw()
        if self.portée > 0:
            pyglet.shapes.Arc(self.position[0], self.position[1], self.taille + self.portée, closed=True, color=(255, 0, 0, 150)).draw()

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return self.nom

    def change_portée(self, newportée):
        self.portée = newportée


class Sort_zone_carré:
    def __init__(self, longueur, largeur, position, durée=1):
        self.longueur = longueur
        self.largueur = largeur
        self.position = position
        self.forme = pyglet.shapes.Rectangle(self.position[0], self.position[1], self.longueur, self.largueur, color=(255, 153, 51, 100))
        self.forme.anchor_position = (self.longueur/2, self.largueur/2)

    def draw(self):
        self.forme.draw()

    def move(self, new_position):
        self.position = new_position
        self.forme = pyglet.shapes.Rectangle(self.position[0], self.position[1], self.longueur, self.largueur, color=(255, 153, 51, 100))
        self.forme.anchor_position = (self.longueur/2, self.largueur/2)


class Sort_zone_cercle:
    def __init__(self, rayon, position, durée=1):
        self.rayon = rayon
        self.position = position

    def draw(self):
        pyglet.shapes.Circle(self.position[0], self.position[1], self.rayon, color=(255, 153, 51, 100)).draw()

    def move(self, new_position):
        self.position = new_position


class Sort_zone_cône:
    def __init__(self, rayon, angle, orientation, position, durée=1):
        self.rayon = rayon
        self.angle = angle
        self.position = position
        self.orientation = orientation

    def draw(self):
        pyglet.shapes.Sector(self.position[0], self.position[1], self.rayon, angle=self.angle, start_angle=self.orientation, color=(255, 153, 51, 100)).draw()

    def move(self, new_orientation):
        self.orientation = new_orientation


window = Champdebataille()
window.add_combattant(Personnage('Gronwall', (0, 102, 204, 255), 0.5, 1.5, 7.5, (400, 400), 0, 3))
window.add_combattant(Personnage('Nyre', (0, 102, 204, 255), 0.5, 1.5, 10, (440, 400), 45, 10))
window.add_combattant(Personnage('Nour', (0, 102, 204, 255), 0.5, 1.5, 9, (350, 400), 0, 7))
pyglet.app.run()
