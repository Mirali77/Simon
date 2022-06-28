import init
from tile import *
from supply import Frame


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instance:
            Singleton.__instance[cls] = cls.__new__(cls)
            Singleton.__instance[cls].__init__(*args, **kwargs)
        return Singleton.__instance[cls]


class TileTable(metaclass=Singleton):
    def __init__(self):
        self.table = []
        self.hidden_tiles = []
        for idx1 in range(4):
            four_tiles = []
            for idx2 in range(4):
                four_tiles.append(Tile(105, (idx2 * 108 + 108, idx1 * 108 + 108), init.all_sprites))
            self.table.append(four_tiles)

    def create_picture(self, lvl: int):
        counter = lvl + 3
        while counter > 0:
            idx1, idx2 = random.randint(0, 3), random.randint(0, 3)
            if self.table[idx1][idx2].color_ind == 0:
                self.table[idx1][idx2].set_color(random.randint(1, 4))
                self.hidden_tiles.append((idx1, idx2))
                counter -= 1

    def check(self):
        return len(self.hidden_tiles) == 0

    def choose_tile(self, click, chosen_color_ind):
        if chosen_color_ind != 0:
            for idx1 in range(4):
                for idx2 in range(4):
                    if self.table[idx1][idx2].rect.collidepoint(click.pos):
                        if self.table[idx1][idx2].color_ind == chosen_color_ind:
                            self.table[idx1][idx2].paint(idx_to_color(chosen_color_ind))
                            self.hidden_tiles.remove((idx1, idx2))
                            return True
                        else:
                            return False
        return True

    def show(self):
        for idx1 in range(4):
            for idx2 in range(4):
                self.table[idx1][idx2].paint(idx_to_color(self.table[idx1][idx2].color_ind))

    def hide(self):
        for idx1 in range(4):
            for idx2 in range(4):
                self.table[idx1][idx2].paint(init.GREY)

    def clear(self):
        for idx1 in range(4):
            for idx2 in range(4):
                self.table[idx1][idx2].set_color(0)
                self.table[idx1][idx2].paint(init.GREY)
        self.hidden_tiles.clear()


class TilePanel(metaclass=Singleton):
    def __init__(self):
        self.panel = []
        for idx in range(4):
            self.panel.append(Tile(70, (idx * 75 + 155, 650), init.all_sprites))
            self.panel[idx].set_color(idx + 1)
            self.panel[idx].paint(idx_to_color(self.panel[idx].color_ind))
        self.chosen_color = None
        self.frame = Frame((70, 70), init.PURPLE)

    def choose_color(self, click):
        for idx in range(4):
            if self.panel[idx].rect.collidepoint(click.pos):
                if self.chosen_color is not None and self.chosen_color.color_ind == self.panel[idx].color_ind:
                    self.chosen_color = None
                    self.frame.visible = False
                else:
                    self.chosen_color = self.panel[idx]
                    self.frame.set_place((self.chosen_color.rect.x, self.chosen_color.rect.y))
                    self.frame.visible = True

    def get_chosen_color(self):
        if self.chosen_color is None:
            return 0
        else:
            return self.chosen_color.color_ind


def idx_to_color(idx: int):
    if idx == 0:
        return init.GREY
    elif idx == 1:
        return init.RED
    elif idx == 2:
        return init.YELLOW
    elif idx == 3:
        return init.GREEN
    elif idx == 4:
        return init.BLUE
