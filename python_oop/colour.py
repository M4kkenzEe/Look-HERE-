from abc import ABC, abstractproperty, abstractmethod


class colour(ABC):

    def __init__(self):
        self.x = None

    @property
    def paint(self):
        pass

    @paint.getter
    def paint(self):
        return self.x

    @paint.setter
    def paint(self, value):
        self.x = value





