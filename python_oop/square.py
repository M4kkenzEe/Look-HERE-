from python_oop.rectangle import rectangle


class square(rectangle):
    _name = "Квадрат"

    def __init__(self, a, col):
        super().__init__(a, a, col)

    @property
    def s(self):
        return self.a ** 2

    @property
    def show_name(self):
        return self._name

    def __repr__(self):
        return 'Название: {}\nПлощадь: {}\nЦвет: {}\n'.format(self.show_name, self.s, self.col)
