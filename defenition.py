#   импорт всех модулей

from pygame import Surface, Rect
from pygame import QUIT, MOUSEBUTTONUP, MOUSEBUTTONDOWN, FULLSCREEN, DOUBLEBUF
from pygame import time, display, event, mouse
from pygame import init as pygame_init
from pygame import font

from random import randint

import sys


#    константы
GLOBAL_SIZE = (1000, 750)
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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRIGHT_BLUE = (55, 155, 255)


#    остальные константы
DELAY = 0.1  # задержка между изменениями таблицы
SPEED_RUN = 5  # количество дней в секунду - не работает
NUMBER_OF_CELLS = 100
FPS = 100  # количество кадров в секунду
IPS = 100  # количество итераций в секунду
CHANCE = 20  # шанс на появление живой клетки при генерации %
Birth, Survive = [5, 6, 7, 8], [4, 5, 6, 7, 8]
# кол-во живых соседей для зарождения жизни, кол-во живых соседей для выживания
TYPE_NEIGHBORS = "8"  # 8 - по сторонам и диагоналям, 4 - по сторонам

# 3/12345 - лабиринт
# 3/23 - жизнь
# 5678/45678 - пещеры
