from python_oop.colour import colour
from python_oop.geo_fig import geo_fig


class rectangle(geo_fig, colour):

    _name = "Прямоугольник"

    def __init__(self, a, b, col):
        self.a = a
        self.b = b
        self.c = colour()
        self.col = col

    @property
    def s(self):
        return self.a * self.b

    @property
    def show_name(self):
        return self._name

    def __repr__(self):
        return 'Название: {}\nПлощадь: {}\nЦвет: {}\n'.format(self.show_name, self.s, self.col)



