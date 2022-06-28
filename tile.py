import init
from init import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, place, group: pygame.sprite.Group):
        pygame.sprite.Sprite.__init__(self)
        self.color_ind = 0
        self.image = pygame.Surface((size, size))
        self.image.fill(init.GREY)
        self.rect = self.image.get_rect()
        self.place = place
        self.rect.center = place
        self.add(group)

    def paint(self, color):
        self.image.fill(color)

    def set_color(self, color_ind):
        self.color_ind = color_ind
