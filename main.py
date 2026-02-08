import pyglet
from classes.champdebataille import Champdebataille
from classes.creature import Personnage
from classes.sorts import Sort_zone_cercle


window = Champdebataille()
window.add_combattant(
    Personnage("Gronwall", (0, 102, 204, 255), 0.5, 1.5, 7.5, (400, 400), 0, 3)
)
window.add_combattant(
    Personnage("Nyre", (255, 102, 204, 255), 0.5, 1.5, 10, (440, 400), 45, 10)
)
window.add_combattant(
    Personnage("Nour", (0, 102, 0, 255), 0.5, 1.5, 9, (350, 400), 0, 7)
)
window.add_zone(Sort_zone_cercle(rayon=500, position=(200, 350), durée=3))
pyglet.app.run()
