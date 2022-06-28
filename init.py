import pygame
import random
from tile_structures import TileTable, TilePanel
from text import Text

WIDTH = 540  # ширина игрового окна
HEIGHT = 720  # высота игрового окна
FPS = 30  # частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
LIGHT_GREY = (192, 192, 192)
PURPLE = (128, 0, 255)
CYAN = (0, 255, 255)

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
images = []
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

tile_table = TileTable()
tile_panel = TilePanel()
chosen_color_ind = tile_panel.get_chosen_color()
game_round = False
level = 0
showing_timer = 0
game = True

gio_message = Text(54, (WIDTH / 2, HEIGHT / 2 - 60), "GAME IS OVER", BLACK, YELLOW)
pa_message = Text(36, (WIDTH / 2, HEIGHT / 2 + 10), "Play again?", BLACK, CYAN)
yes_message = Text(36, (WIDTH / 2 - 40, HEIGHT / 2 + 60), "YES", BLACK, GREEN)
no_message = Text(36, (WIDTH / 2 + 40, HEIGHT / 2 + 60), "NO", BLACK, RED)
level_message = Text(36, (WIDTH / 2, HEIGHT / 2 + 190), "LEVEL: " + str(level), BLACK, LIGHT_GREY)