import init
from init import *


class Frame:
    def __init__(self, size, color):
        self.parts = []
        self.size = size
        width = size[0]
        height = size[1]
        self.parts.append(pygame.Surface((4, size[1])))
        self.parts.append(pygame.Surface((size[0], 4)))
        self.parts.append(pygame.Surface((size[0], 4)))
        self.parts.append(pygame.Surface((4, size[1])))
        for ind in self.parts:
            ind.fill(color)
        self.visible = False

    def draw(self, place):
        if self.visible:
            init.screen.blit(self.parts[0], place)
            init.screen.blit(self.parts[1], place)
            init.screen.blit(self.parts[2], (place[0], place[1] + self.size[1] - 4))
            init.screen.blit(self.parts[3], (place[0] + self.size[0] - 4, place[1]))

    def set_place(self, place):
        self.place = place


class Button:
    def __init__(self, size, color):
        self.image = pygame.Surface(size)
        self.image.fill(color)

    def draw(self, place):
        init.screen.blit(self.image, place)

    def change_color(self, color):
        self.image.fill(color)