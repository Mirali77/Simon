import init
from init import *
from supply import Button, Frame


class Text:
    def __init__(self, size: int, place_cord, message_str: str, colour, button_color):
        self.font = pygame.font.Font(None, size)
        self.message = self.font.render(message_str, True, colour)
        self.rect = self.message.get_rect(center=place_cord)
        self.text = message_str
        self.place_cord = place_cord
        self.button_color = button_color
        self.button = Button((self.rect.width + 10, self.rect.height + 10), button_color)
        self.frame = Frame((self.rect.width + 10, self.rect.height + 10), init.BLACK)
        self.frame.visible = True

    def draw(self):
        self.button.draw((self.rect.x - 5, self.rect.y - 5))
        self.frame.draw((self.rect.x - 5, self.rect.y - 5))
        init.screen.blit(self.message, self.rect)

    def set_message(self, message_str):
        self.message = self.font.render(message_str, True, init.BLACK)
        self.rect = self.message.get_rect(center=self.place_cord)
        self.text = message_str

    def update(self, color):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.button.change_color(color)
        else:
            self.button.change_color(self.button_color)
