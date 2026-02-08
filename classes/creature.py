import pyglet


class Personnage:
    def __init__(
        self,
        nom="",
        couleur=(0, 102, 204, 255),
        taille=1.5,
        allonge=1.5,
        basespeed=9,
        position=(0, 0),
        portée=0,
        initiative=5,
    ):
        self.couleur = couleur
        self.taille = taille * 10
        self.nom = nom
        self.allonge = allonge * 10
        self.position = position
        self.position_save = position
        self.position_tour = position
        self.basespeed = basespeed * 10
        self.speed = basespeed * 10
        self.portée_base = portée * 10
        self.portée = portée
        self.initiative = initiative

    def draw(self):
        pyglet.shapes.Circle(
            self.position[0],
            self.position[1],
            self.taille + self.allonge,
            color=(204, 0, 0, 150),
        ).draw()
        pyglet.shapes.Circle(
            self.position[0], self.position[1], self.taille, color=self.couleur
        ).draw()

    def draw_selected(self):
        pyglet.shapes.Arc(
            self.position_save[0],
            self.position_save[1],
            self.taille + self.speed,
            closed=True,
            color=(0, 204, 0, 150),
        ).draw()
        if self.portée > 0:
            pyglet.shapes.Arc(
                self.position[0],
                self.position[1],
                self.taille + self.portée,
                closed=True,
                color=(255, 0, 0, 150),
            ).draw()

    def move(self, new_position):
        self.position = new_position

    def __str__(self):
        return self.nom

    def change_portée(self, newportée):
        self.portée = newportée
