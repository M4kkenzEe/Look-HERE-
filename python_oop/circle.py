import math
from python_oop.colour import colour
from python_oop.geo_fig import geo_fig


class circle(geo_fig, colour):
    _name = "Окружность"

    def __init__(self, r, col):
        self.r = r
        self.c = colour()
        self.col = col

    @property
    def s(self):
        return (self.r ** 2) * math.pi

    @property
    def show_name(self):
        return self._name

    def __repr__(self):
        return 'Название: {}\nПлощадь: {}\nЦвет: {}\n'.format(self.show_name, self.s, self.col)



