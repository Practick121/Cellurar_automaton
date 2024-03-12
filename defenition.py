#   импорт всех модулей
from pygame import Surface, Rect
from pygame import QUIT, MOUSEBUTTONUP, MOUSEBUTTONDOWN, DOUBLEBUF
from pygame import time, display, event, mouse
from pygame import init as pygame_init
from pygame import font
from random import randint
import sys

#    константы
GLOBAL_SIZE = (900, 750)
TABLE_SIZE = (750, 750)
TITLE = "Клеточный автомат"
font_list = {'normal': (None, 15),
             'buttons': (None, 20),
             }  # словарь шрифтов
SEC = 1000
FLAGS = DOUBLEBUF
RUN = 1
STOP = 0
RUN_ONE_STEP = 2
CLEAN = 3
GENERATE = 4

#    цвета
GRAY = (128, 128, 128)
GREEN = (0, 204, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRIGHT_BLUE = (55, 155, 255)

#    остальные константы
NAME = 'data.txt'  # имя открываемого файла
GRID = True  # True - сетка отображается
# (даже при False сетка может отображаться из-за погрешности размера клетки)
LIVE_COLOR = BLACK  # цвет живых клеток
DEATH_COLOR = WHITE  # цвет мертвых клеток
DELAY = 0.05  # задержка между изменениями таблицы
NUMBER_OF_CELLS = 100  # количество клеток на одной стороне квадрата
FPS = 60  # количество кадров в секунду
IPS = 10000  # количество итераций в секунду
CHANCE = 50  # шанс на появление живой клетки при генерации (%)
Birth, Survive = [5, 6, 7, 8], [4, 5, 6, 7, 8]
# кол-во живых соседей для зарождения жизни, кол-во живых соседей для выживания
TYPE_NEIGHBORS = "8"  # 8 - по сторонам и диагоналям, 4 - по сторонам
