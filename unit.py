import pygame.gfxdraw
class Unit:
    def __init__(self):
        self.state = False

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def alive(self):
        self.state = True

    def die(self):
        self.state = False

    def draw(self, x =0, y=0, size=5, screen = None):
        if self.state:
            pygame.gfxdraw.box(screen, ((x, y), (size, size)), (0, 0, 0))
        else:
            pygame.gfxdraw.box(screen, ((x, y), (size, size)), (255, 255, 255))



