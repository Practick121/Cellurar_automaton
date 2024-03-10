from defenition import Surface, Rect, Survive, Birth
from defenition import BLACK, WHITE, BRIGHT_BLUE, CHANCE, TABLE_SIZE, NUMBER_OF_CELLS, TYPE_NEIGHBORS, SEC, DELAY
from defenition import RUN, RUN_ONE_STEP, GENERATE, CLEAN, STOP
from defenition import randint, font, font_list, mouse, time


class Sprite:
    def render(self, window):
        pass

    def check(self):
        pass


class Cell:

    def __init__(self, coord, size, health):
        self.surf = Surface(size)
        self.rect = self.surf.get_rect(topleft=coord)
        self.health = health

    def render(self, window):
        if self.health:
            self.surf.fill(BLACK)
        else:
            self.surf.fill(WHITE)
        window.blit(self.surf, self.rect)

    def set_health(self, health):
        self.health = health

    def change_health(self):
        self.health = 1 - self.health

    def get_health(self):
        return self.health

    def get_coord(self):
        return self.rect.topleft


class Table(Sprite):
    status = STOP

    def generate(self):
        for i in range(self.cnt_cells):
            for j in range(self.cnt_cells):
                if self.cnt_cells / 2 - 8 <= i <= self.cnt_cells / 2 + 8 and self.cnt_cells / 2 - 8 <= j <= self.cnt_cells / 2 + 8:
                    health = int(randint(1, 100) <= CHANCE)
                else:
                    health = 0
                #health = int(randint(1, 100) <= CHANCE)
                self.matrix[i][j] = health

    def clean(self):
        for i in range(self.cnt_cells):
            for j in range(self.cnt_cells):
                self.matrix[i][j] = 0

    def __init__(self, size=TABLE_SIZE, coord=(0, 0), cnt_cells=NUMBER_OF_CELLS):
        self.matrix: list[list[int]] = []
        self.matrix = [[0 for _ in range(cnt_cells)] for __ in range(cnt_cells)]
        self.size = size
        self.cnt_cells = cnt_cells
        self.cell_size = (size[0] / cnt_cells, size[1] / cnt_cells)
        self.generate()
        self.surf = Surface(TABLE_SIZE)
        self.rect = self.surf.get_rect(topleft=coord)
        self.last_touch = (-1, -1)

    def get_cell_rect(self, j, i, grand=False):
        if not grand:
            return Rect(j * self.cell_size[0], i * self.cell_size[1], *self.cell_size)
        else:
            return Rect(j * self.cell_size[0] + self.rect.left, i * self.cell_size[1] + self.rect.top, *self.cell_size)

    def render(self, window):
        for i in range(self.cnt_cells):
            for j in range(self.cnt_cells):
                crd = (j * self.cell_size[0], i * self.cell_size[1])
                cell = Cell(crd, (self.cell_size[0] - 1, self.cell_size[1] - 1), self.matrix[i][j])
                cell.render(self.surf)
        window.blit(self.surf, self.rect)

    def cnt_neighbors(self, x, y):
        number = 0
        number += int(y > 0 and self.matrix[y - 1][x])
        number += int(x > 0 and self.matrix[y][x - 1])
        number += int(x < self.cnt_cells - 1 and self.matrix[y][(x + 1)])
        number += int(y < self.cnt_cells - 1 and self.matrix[(y + 1) % self.cnt_cells][x])

        if TYPE_NEIGHBORS == '8':
            number += int(y > 0 and x > 0 and self.matrix[y - 1][x - 1])
            number += int(y > 0 and x < self.cnt_cells - 1 and self.matrix[y - 1][
                (x + 1) % self.cnt_cells])
            number += int(y < self.cnt_cells - 1 and x > 0 and self.matrix[(y + 1) % self.cnt_cells][
                x - 1])
            number += int(x < self.cnt_cells - 1 and y < self.cnt_cells - 1 and
                          self.matrix[(y + 1) % self.cnt_cells][(x + 1) % self.cnt_cells])
        return number

    def run_one_step(self):
        new_matrix = []

        for i in range(self.cnt_cells):
            new_matrix.append([])
            for j in range(self.cnt_cells):
                health = self.matrix[i][j]
                cnt = self.cnt_neighbors(j, i)
                if health == 0 and cnt in Transmission.Birth:
                    new_matrix[i].append(1)
                elif health == 1 and cnt not in Transmission.Survive:
                    new_matrix[i].append(0)
                else:
                    new_matrix[i].append(health)

        for i in range(self.cnt_cells):
            for j in range(self.cnt_cells):
                self.matrix[i][j] = new_matrix[i][j]

    def actions_with_mouse(self):
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            j, i = int((pos[0] - self.rect[0]) / self.cell_size[0]), \
                   int((pos[1] - self.rect[1]) / self.cell_size[1])
            if (j, i) != self.last_touch:
                self.matrix[i][j] = 1 - self.matrix[i][j]
                self.last_touch = (j, i)

    def check(self):
        if mouse.get_pressed()[0] and mouse.get_focused():
            self.actions_with_mouse()
        if Table.status == RUN:
            self.run_one_step()
            Table.status = STOP
        elif Table.status == GENERATE:
            self.generate()
            Table.status = STOP
        elif Table.status == CLEAN:
            self.clean()
            Table.status = STOP


class Button(Sprite):
    list = []

    def __init__(self, size: tuple, coord: tuple, color: tuple, text: str = "Button",
                 color_text: tuple = BLACK, func=None):
        # конструктор класса, который принимает размеры и расположение левого правого угла
        # кнопки, ее текст, цвет и функция при нажатии
        self.size = size
        self.func = func
        surf = Surface(size)

        self.rect = surf.get_rect(topleft=coord)
        self.text = text
        self.color_text = color_text
        self.font = font.Font(*font_list['buttons'])
        self.text_surf = self.font.render(text, False, color_text)
        self.text_rect = self.text_surf.get_rect(center=(size[0] / 2, size[1] / 2))
        r, g, b = color
        hover = (max(r - 40, 0), max(g - 40, 0), max(b - 40, 0))
        pressed = (max(r - 60, 0), max(g - 60, 0), max(b - 60, 0))
        self.color = color
        self.colors = {"normal": color, "hover": hover, "pressed": pressed}

        surf1 = surf.copy()
        surf1.fill(self.colors["normal"])
        surf2 = surf.copy()
        surf2.fill(self.colors["hover"])
        surf3 = surf.copy()
        surf3.fill(self.colors["pressed"])
        self.list_surface = {'normal': surf1,
                             'hover': surf2,
                             'pressed': surf3}
        self.type_surf = 'normal'
        # определение всех цветов кнопки при разных обстоятельствах
        self.press = False
        Button.list.append(self)

    def check(self):
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.press:
                self.type_surf = 'pressed'
            else:
                self.type_surf = 'hover'
        else:
            self.type_surf = 'normal'

    def press_down(self):
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.press = True
            self.type_surf = 'pressed'
            self.func()
        else:
            self.type_surf = 'normal'

    def press_up(self):
        pos = mouse.get_pos()
        self.press = False
        if self.rect.collidepoint(pos):
            self.type_surf = 'hover'

    def render(self, surface):
        but_surf = self.list_surface[self.type_surf]
        but_surf.blit(self.text_surf, self.text_rect)
        surface.blit(but_surf, self.rect)


class Timer:

    def __init__(self, timer):  # в секундах
        self.start = time.get_ticks()
        self.time = timer

    def wind_up(self):
        self.start = time.get_ticks()

    def is_out(self):
        if time.get_ticks() >= self.start + self.time * SEC:
            return True
        return False


class Transmission:
    paintstop = False
    gl_status = 0
    Birth = []
    Survive = []
    delay_timer = Timer(DELAY)


class ActiveButton(Button):  # специфические кнопки находятся в группах: активная кнопка горит отдельным цветом
    def __init__(self, *args, mas, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.active = False
        self.colors['active'] = BRIGHT_BLUE
        surf = Surface(self.size)
        surf.fill(BRIGHT_BLUE)
        self.list_surface['active'] = surf
        mas.append(self)
        self.mas = mas

    def get_active(self):
        self.active = True
        for button in self.mas:
            if button != self:
                button.active = False
        self.type_surf = 'active'

    def press_down(self):
        Button.press_down(self)
        if self.press:
            self.active = True
        if self.active:
            self.get_active()

    def press_up(self):
        self.press = False

    def check(self):
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos) and not self.active:
            if self.press:
                self.type_surf = 'pressed'
            else:
                self.type_surf = 'hover'
        elif not self.active:
            self.type_surf = 'normal'
        else:
            self.type_surf = 'active'
