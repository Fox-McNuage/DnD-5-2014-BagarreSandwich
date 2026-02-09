import pyglet


class Sort_zone_carré:
    def __init__(self, longueur, largeur, position, durée=1):
        self.longueur = longueur
        self.largueur = largeur
        self.position = position
        self.forme = pyglet.shapes.Rectangle(
            self.position[0],
            self.position[1],
            self.longueur,
            self.largueur,
            color=(255, 153, 51, 100),
        )
        self.forme.anchor_position = (self.longueur/2, self.largueur/2)

    def draw(self):
        self.forme.draw()

    def move(self, new_position):
        self.position = new_position
        self.forme = pyglet.shapes.Rectangle(
            self.position[0],
            self.position[1],
            self.longueur,
            self.largueur,
            color=(255, 153, 51, 100),
        )
        self.forme.anchor_position = (self.longueur/2, self.largueur/2)


class Sort_zone_cercle:
    def __init__(self, rayon, position, durée=1):
        self.rayon = rayon
        self.position = position

    def draw(self):
        pyglet.shapes.Circle(
            self.position[0], self.position[1], self.rayon, color=(255, 153, 51, 100)
        ).draw()

    def move(self, new_position):
        self.position = new_position


class Sort_zone_cône:
    def __init__(self, rayon, angle, orientation, position, durée=1):
        self.rayon = rayon
        self.angle = angle
        self.position = position
        self.orientation = orientation

    def draw(self):
        pyglet.shapes.Sector(
            self.position[0],
            self.position[1],
            self.rayon,
            angle=self.angle,
            start_angle=self.orientation,
            color=(255, 153, 51, 100),
        )

    def move(self, new_orientation):
        self.orientation = new_orientation
